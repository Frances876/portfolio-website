from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Output path
pdf_path = "/mnt/data/Web_Developer_CV.pdf"

# Styles
styles = getSampleStyleSheet()
style_title = styles['Title']
style_heading = styles['Heading2']
style_normal = styles['BodyText']

# Build document
doc = SimpleDocTemplate(pdf_path, pagesize=A4)
content = []

# Title
content.append(Paragraph("John Doe - Web Developer", style_title))
content.append(Spacer(1, 12))

# Contact Info
contact_info = """
📍 Lagos, Nigeria<br />
📞 +234 000 000 0000<br />
📧 johndoe@email.com<br />
🌐 github.com/johndoe | linkedin.com/in/johndoe
"""
content.append(Paragraph(contact_info, style_normal))
content.append(Spacer(1, 12))

# Summary
content.append(Paragraph("Professional Summary", style_heading))
summary = """
Creative and detail-oriented Web Developer with hands-on experience building responsive, user-friendly websites using
HTML, CSS, and JavaScript.
Skilled at transforming design concepts into efficient code and optimizing performance for speed and accessibility.
Passionate about front-end development, UI/UX design, and continuous learning in modern web technologies.
"""
content.append(Paragraph(summary, style_normal))
content.append(Spacer(1, 12))

# Skills
content.append(Paragraph("Technical Skills", style_heading))
skills = """
<b>Languages:</b> HTML5, CSS3, JavaScript (ES6+)<br />
<b>Frameworks & Tools:</b> Bootstrap, Tailwind CSS, Git, VS Code<br />
<b>Core Skills:</b> Responsive Design, DOM Manipulation, API Integration, Web Accessibility<br />
<b>Currently Learning:</b> React.js, Node.js
"""
content.append(Paragraph(skills, style_normal))
content.append(Spacer(1, 12))

# Projects
content.append(Paragraph("Projects", style_heading))
projects = """
<b>1. Movie Discovery App</b><br />
Built a web app using the TMDb API to fetch and display movie data dynamically.<br />
Implemented responsive Swiper.js sliders and YouTube trailer integration.<br />
<i>Tech Used:</i> HTML, CSS, JavaScript, Fetch API.<br /><br />

<b>2. Personal Portfolio Website</b><br />
Designed and developed a responsive portfolio website to showcase projects and skills.<br />
Used smooth scrolling, modern layout, and mobile-first design principles.<br /><br />

<b>3. To-Do List Web App</b><br />
Created an interactive to-do app with add, edit, and delete features.<br />
Integrated localStorage for persistent data management.
"""
content.append(Paragraph(projects, style_normal))
content.append(Spacer(1, 12))

# Education
content.append(Paragraph("Education", style_heading))
education = """
<b>Diploma in Web Development</b> — Lagos Tech Institute<br />
2024
"""
content.append(Paragraph(education, style_normal))
content.append(Spacer(1, 12))

# Certifications
content.append(Paragraph("Certifications", style_heading))
certs = """
- HTML, CSS, and JavaScript for Web Developers — Coursera<br />
- Responsive Web Design — freeCodeCamp
"""
content.append(Paragraph(certs, style_normal))
content.append(Spacer(1, 12))

# Soft Skills
content.append(Paragraph("Soft Skills", style_heading))
soft_skills = """
Problem Solving, Communication, Attention to Detail, Time Management, Team Collaboration
"""
content.append(Paragraph(soft_skills, style_normal))
content.append(Spacer(1, 12))

# References
content.append(Paragraph("References", style_heading))
content.append(Paragraph("Available upon request", style_normal))

# Build PDF
doc.build(content)

pdf_path