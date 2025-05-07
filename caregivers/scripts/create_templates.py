import os

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), '../templates/caregivers')
TEMPLATE_DIR = os.path.abspath(TEMPLATE_DIR)

os.makedirs(TEMPLATE_DIR, exist_ok=True)

files = {
    'base.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Caregiver Management{% endblock %}</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-4">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
''',
    'caregiver_list.html': '''{% extends "caregivers/base.html" %}
{% block content %}
  <h1>Caregivers</h1>
  <ul>
    {% for caregiver in object_list %}
      <li>
        <a href="{% url 'caregiver_detail' caregiver.pk %}">{{ caregiver.name }}</a>
      </li>
    {% endfor %}
  </ul>
  <a href="{% url 'caregiver_add' %}" class="btn btn-primary">Add Caregiver</a>
{% endblock %}
''',
    'caregiver_detail.html': '''{% extends "caregivers/base.html" %}
{% block content %}
  <h1>{{ object.name }}</h1>
  <p>Agency: {{ object.agency }}</p>
  <p>Specialties: {{ object.specialties }}</p>
  <p>Status: {{ object.status|yesno:"Active,Inactive" }}</p>
  <a href="{% url 'caregiver_edit' object.pk %}" class="btn btn-secondary">Edit</a>
  <a href="{% url 'caregiver_list' %}" class="btn btn-link">Back to list</a>
{% endblock %}
''',
    'caregiver_form.html': '''{% extends "caregivers/base.html" %}
{% block content %}
  <h1>{% if object %}Edit{% else %}Add{% endif %} Caregiver</h1>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-success">Save</button>
    <a href="{% url 'caregiver_list' %}" class="btn btn-link">Cancel</a>
  </form>
{% endblock %}
''',
}

for filename, content in files.items():
    with open(os.path.join(TEMPLATE_DIR, filename), 'w') as f:
        f.write(content)

print(f"Created templates in {TEMPLATE_DIR}")
