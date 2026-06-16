# Split
sentence = "Hello, Good afternoon, and thank you for giving me this opportunity to introduce myself. My name is Chandan Prasad. I am a Computer Engineering professional with over 15 years of experience spanning academia, technical training, software development, curriculum design, and research. Currently, I have completed the submission of my Ph.D. thesis in Computer Engineering and have been actively involved in teaching, mentoring, and academic leadership roles.Throughout my career, I have worked as an Assistant Professor, Technical Trainer, Program Lead, and Subject Matter Expert. I have delivered courses in Java Programming, Android Development, Artificial Intelligence, Full Stack Development, Web Technologies, and Software Engineering. I have also mentored more than 3,000 students and guided over 85 faculty members through various certification and skill development initiatives.From a research perspective, I have published 13 Scopus-indexed research papers, achieved an h-index of 4, received 50+ citations, and secured two patents. My research interests include Artificial Intelligence, Deep Learning, Computer Vision, Federated Learning, Blockchain Applications, Cybersecurity, and Smart Healthcare Systems.In addition to teaching and research, I have served as MOOC Coordinator, RedHat Head, and Board of Studies member, contributing to curriculum development, industry collaborations, and academic innovation. I am also certified in Oracle Cloud Infrastructure, Generative AI, Data Science, and DevOps technologies.I strongly believe in outcome-based education, research-driven learning, and bridging the gap between academia and industry. My goal is to contribute to institutional growth through quality teaching, impactful research, student mentorship, and collaborative innovation.Thank you, and I look forward to discussing how my experience and expertise can contribute to your esteemed institution."
print("The sentence is:", sentence)
print("The first character of the sentence is:", sentence.splitlines()[0][0])
print("The length of the sentence is:", len(sentence))
words = sentence.split()
print("The words in the sentence are:", words)
print("The number of words in the sentence is:", len(words))


new_sentence = sentence.replace(" ", "_")
print("The new sentence is:", new_sentence)
# Join
new_sentence = "_".join(words)
new_sentence = new_sentence.upper()
print("The new sentence is:", new_sentence)


text = "I love Java"
print("The original text is:", text)
updated_text = text.replace("Java", "Python")
print("The updated text is:", updated_text)

messy = "     Hello, World     "
print("The messy text is:", messy)
cleaned_text = messy.strip()
print("The cleaned text is:", cleaned_text)