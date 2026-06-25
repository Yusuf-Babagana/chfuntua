from django.db import migrations
from django.conf import settings


def replace_programmes(apps, schema_editor):
    Programme = apps.get_model('portal', 'Programme')
    Application = apps.get_model('portal', 'Application')

    # Delete existing programmes
    Programme.objects.all().delete()

    # Seed the 8 new CHESF programmes
    programmes = [
        {
            'name': 'National Diploma in Community Health (ND-CHEW)',
            'code': 'ND-CHEW',
            'category': 'nd',
            'duration': '3 Years',
            'description': 'Comprehensive national diploma programme training Community Health Extension Workers for primary healthcare delivery in Nigeria.',
            'admission_requirements': 'Five SSCE credits in English, Mathematics, Biology, Chemistry, and Physics at not more than two sittings.',
            'accreditation_body': 'CHPRBN',
            'icon': 'fa-heartbeat',
            'order': 1,
        },
        {
            'name': 'Diploma in Community Health Extension Worker (CHEW)',
            'code': 'CHEW',
            'category': 'dip',
            'duration': '2 Years',
            'description': 'Diploma programme training Community Health Extension Workers for primary healthcare delivery and community health services.',
            'admission_requirements': 'Four SSCE credits including English, Mathematics, Biology, and any other science subject.',
            'accreditation_body': 'CHPRBN',
            'icon': 'fa-user-md',
            'order': 2,
        },
        {
            'name': 'Junior Community Health Extension Workers (JCHEW)',
            'code': 'JCHEW',
            'category': 'cert',
            'duration': '2 Years',
            'description': 'Certificate programme for Junior Community Health Extension Workers providing foundational community health training.',
            'admission_requirements': 'Three SSCE credits including English, Mathematics, and Biology.',
            'accreditation_body': 'CHPRBN',
            'icon': 'fa-certificate',
            'order': 3,
        },
        {
            'name': 'National Diploma in Environmental Health (ND)',
            'code': 'ND-ENV',
            'category': 'nd',
            'duration': '2 Years',
            'description': 'National Diploma in Environmental Health training professionals in sanitation, pollution control, and public health inspection.',
            'admission_requirements': 'Five SSCE credits in English, Mathematics, Biology, Chemistry, and any other subject.',
            'accreditation_body': 'EHCON',
            'icon': 'fa-leaf',
            'order': 4,
        },
        {
            'name': 'Diploma in Environmental Health',
            'code': 'HND-ENV',
            'category': 'hnd',
            'duration': '2 Years',
            'description': 'Diploma in Environmental Health for advanced training in environmental health management and policy.',
            'admission_requirements': 'ND in Environmental Health with at least Lower Credit plus NYSC or five years work experience.',
            'accreditation_body': 'EHCON',
            'icon': 'fa-tree',
            'order': 5,
        },
        {
            'name': 'Diploma in Health Information Management (HIM)',
            'code': 'HIM',
            'category': 'dip',
            'duration': '2 Years',
            'description': 'Diploma in health records management, health informatics, medical coding, and health data administration.',
            'admission_requirements': 'Four SSCE credits including English, Mathematics, Biology, and any other subject.',
            'accreditation_body': 'WAHEB',
            'icon': 'fa-notes-medical',
            'order': 6,
        },
        {
            'name': 'Diploma in Health Promotion & Education (HPE)',
            'code': 'HPE',
            'category': 'dip',
            'duration': '2 Years',
            'description': 'Diploma in health promotion, community health education, and behaviour change communication.',
            'admission_requirements': 'Four SSCE credits including English, Mathematics, Biology, and any other subject.',
            'accreditation_body': 'WAHEB',
            'icon': 'fa-chalkboard-teacher',
            'order': 7,
        },
        {
            'name': 'Diploma in Public Health (DPH)',
            'code': 'DPH',
            'category': 'dip',
            'duration': '2 Years',
            'description': 'Diploma in public health for disease prevention, health policy, and community health programme management.',
            'admission_requirements': 'Four SSCE credits including English, Mathematics, Biology, and any other subject.',
            'accreditation_body': 'WAHEB',
            'icon': 'fa-shield-virus',
            'order': 8,
        },
    ]
    for data in programmes:
        Programme.objects.create(**data)

    # Reset draft applications with old course choice values
    old_courses = [
        'nd_chew', 'dip_env_health', 'dip_him', 'dip_xray',
        'dip_nutrition', 'cert_jchew', 'retraining_jchew', 'dip_pharmacy'
    ]
    draft_apps = Application.objects.filter(status='draft')
    for app in draft_apps:
        changed = False
        if app.first_choice in old_courses:
            app.first_choice = ''
            changed = True
        if app.second_choice in old_courses:
            app.second_choice = ''
            changed = True
        if changed:
            app.section_d_completed = False
            app.save()


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_seed_programmes'),
    ]

    operations = [
        migrations.RunPython(replace_programmes),
    ]
