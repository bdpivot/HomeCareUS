import re
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import spacy
from dateutil import parser as date_parser
from .models import CaregiverExperience, Skill, Certification

class ResumeParserService:
    def __init__(self):
        # Load English language model
        self.nlp = spacy.load("en_core_web_sm")
        
        # Common caregiver skills and their variations
        self.skill_patterns = {
            'personal_care': ['personal care', 'bathing', 'dressing', 'grooming', 'hygiene'],
            'medication': ['medication', 'medication administration', 'medication management'],
            'mobility': ['mobility', 'transfer', 'ambulation', 'wheelchair'],
            'meal_prep': ['meal preparation', 'cooking', 'nutrition', 'feeding'],
            'housekeeping': ['housekeeping', 'cleaning', 'laundry', 'household tasks'],
            'companionship': ['companionship', 'social support', 'emotional support'],
            'medical': ['vital signs', 'blood pressure', 'temperature', 'pulse'],
            'dementia': ['dementia', 'alzheimer', 'memory care'],
            'hospice': ['hospice', 'end of life', 'palliative care'],
            'specialized': ['special needs', 'developmental disabilities', 'mental health']
        }

    def parse_resume(self, resume_text: str) -> Dict:
        """
        Parse resume text and extract relevant information
        """
        doc = self.nlp(resume_text)
        
        # Extract experiences
        experiences = self._extract_experiences(doc)
        
        # Extract skills
        skills = self._extract_skills(doc)
        
        # Extract certifications
        certifications = self._extract_certifications(doc)
        
        return {
            'experiences': experiences,
            'skills': skills,
            'certifications': certifications
        }

    def _extract_experiences(self, doc) -> List[Dict]:
        """
        Extract work experiences from resume text
        """
        experiences = []
        current_experience = None
        
        # Look for date patterns
        date_pattern = r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{4}\b'
        
        for sent in doc.sents:
            # Check if this is a new experience entry
            if re.search(date_pattern, sent.text):
                if current_experience:
                    experiences.append(current_experience)
                
                # Try to extract dates
                dates = re.findall(date_pattern, sent.text)
                if len(dates) >= 2:
                    try:
                        start_date = date_parser.parse(dates[0])
                        end_date = date_parser.parse(dates[1])
                        is_current = False
                    except:
                        continue
                elif len(dates) == 1:
                    try:
                        start_date = date_parser.parse(dates[0])
                        end_date = None
                        is_current = True
                    except:
                        continue
                else:
                    continue
                
                # Extract employer and position
                employer = None
                position = None
                
                # Look for common employer indicators
                employer_indicators = ['at', 'with', 'for']
                for indicator in employer_indicators:
                    if indicator in sent.text:
                        parts = sent.text.split(indicator)
                        position = parts[0].strip()
                        employer = parts[1].strip()
                        break
                
                if not employer or not position:
                    continue
                
                current_experience = {
                    'employer_name': employer,
                    'position': position,
                    'start_date': start_date,
                    'end_date': end_date,
                    'is_current': is_current,
                    'description': ''
                }
            elif current_experience:
                current_experience['description'] += sent.text + ' '
        
        if current_experience:
            experiences.append(current_experience)
        
        return experiences

    def _extract_skills(self, doc) -> List[str]:
        """
        Extract skills from resume text
        """
        skills = set()
        
        for sent in doc.sents:
            text = sent.text.lower()
            
            for category, patterns in self.skill_patterns.items():
                for pattern in patterns:
                    if pattern in text:
                        skills.add(pattern)
        
        return list(skills)

    def _extract_certifications(self, doc) -> List[Dict]:
        """
        Extract certifications from resume text
        """
        certifications = []
        
        # Common certification patterns
        cert_patterns = [
            r'(?:CNA|HHA|LPN|RN|CPR|First Aid|BLS|ACLS)',
            r'Certified (?:Nursing Assistant|Home Health Aide|Medical Assistant)',
            r'Licensed (?:Practical Nurse|Registered Nurse)'
        ]
        
        for sent in doc.sents:
            for pattern in cert_patterns:
                if re.search(pattern, sent.text, re.IGNORECASE):
                    # Try to extract dates
                    date_pattern = r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{4}\b'
                    dates = re.findall(date_pattern, sent.text)
                    
                    if len(dates) >= 1:
                        try:
                            issue_date = date_parser.parse(dates[0])
                            expiry_date = date_parser.parse(dates[1]) if len(dates) > 1 else None
                            
                            cert = {
                                'name': re.search(pattern, sent.text, re.IGNORECASE).group(),
                                'issuing_organization': 'Unknown',  # Would need more context to determine
                                'issue_date': issue_date,
                                'expiry_date': expiry_date,
                                'is_current': True if not expiry_date else expiry_date > datetime.now()
                            }
                            certifications.append(cert)
                        except:
                            continue
        
        return certifications

    def create_experience_objects(self, caregiver, parsed_data: Dict) -> Tuple[List[CaregiverExperience], List[Skill], List[Certification]]:
        """
        Create database objects from parsed resume data
        """
        # Create skills
        skills = []
        for skill_name in parsed_data['skills']:
            skill, _ = Skill.objects.get_or_create(
                name=skill_name,
                defaults={'category': 'caregiving'}
            )
            skills.append(skill)
        
        # Create certifications
        certifications = []
        for cert_data in parsed_data['certifications']:
            cert, _ = Certification.objects.get_or_create(
                name=cert_data['name'],
                issuing_organization=cert_data['issuing_organization'],
                defaults={
                    'issue_date': cert_data['issue_date'],
                    'expiry_date': cert_data['expiry_date'],
                    'is_current': cert_data['is_current']
                }
            )
            certifications.append(cert)
        
        # Create experiences
        experiences = []
        for exp_data in parsed_data['experiences']:
            experience = CaregiverExperience.objects.create(
                caregiver=caregiver,
                employer_name=exp_data['employer_name'],
                position=exp_data['position'],
                start_date=exp_data['start_date'],
                end_date=exp_data['end_date'],
                is_current=exp_data['is_current'],
                description=exp_data['description']
            )
            experience.skills.set(skills)
            experience.certifications.set(certifications)
            experiences.append(experience)
        
        return experiences, skills, certifications 