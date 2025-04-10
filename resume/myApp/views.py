from django.shortcuts import render

# Create your views here.
def resume(request):
    resumeData = {
        'name': 'Nimijith Nimmi Jayan',
        'role': 'Python Developer',
        'contact': {
            'address1': 'HH.155, Lord Home Hall',
            'address2': 'Edinburgh, Scotland, UK',
            'postcode': 'EH14 4AS',
            'phone': '+44 7979 247296',
            'email': 'njnimijith@gmail.com',
        },
        'education': {
            'degree': 'M.Sc in Artificial Intelligence',
            'college': 'Heriot-Watt University, Edinburgh',
            'coursework': [
                'Python Programming', 'Machine Learning', 'Web Development with Django',
                'Discrete Mathematics', 'Java Programming', 'Project Management'
            ]
        },
        'skills': {
            'communication': 'Over 10 years experience in customer service; skilled at conveying technical concepts clearly.',
            'leadership': 'Led automation initiatives at India Post; organised code sprints during group projects.',
        },
        'experience': [
            {'period': 'Feb 2025 – Present', 'position': 'Python Developer Intern', 'company': 'CodeNest AI'},            
            {'period': '2011 – 2024', 'position': 'Postal Assistant', 'company': 'India Post'},
        ],
        'gender': 'female',
        'references': 'Available upon request',
    }
    return render(request, 'resume.html', resumeData)