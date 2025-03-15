---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

Nice to meet you! I am Feiyang Hao (郝飞洋), currently a third year undergraduate student studying software engineering in Xi'an Jiaotong University.

My research interests lie in multimodal models and human-ai interaction.

"Stay hungry, stay foolish." I have hunger for adventure, and I think learning is a journey of a lifetime.


# 🔥 News
- *Mar 2025*: &nbsp; 📝 I am pleased to share that our work, CalliReader, is now available on [arXiv](https://arxiv.org/abs/2503.06472)
- *Dec 2024*: &nbsp; 🌟 Exchange program concluded, but exploration continues!  
- *Sep 2024*: &nbsp; 🎉 Started exchange semester at HKU (The University of Hong Kong)!  
- *Apr 2024*: &nbsp; 🚀 Started research internship in Wangxuan Institute of Computer Technology, PKU guided by Prof. Zhouhui Lian!  

# 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Pre-print</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[CalliReader: Contextualizing Chinese Calligraphy via an Embedding-Aligned Vision-Language Model](https://arxiv.org/pdf/2503.06472)

Yuxuan Luo, Jiaqi Tang, Chenyi Huang, **Feiyang Hao**, Zhouhui Lian

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=DhtAFkwAAAAJ&citation_for_view=DhtAFkwAAAAJ:ALROH1vI_8AC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
</div>
</div>

- [Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet](https://github.com), A, B, C, **CVPR 2020**

# 🎖 Selected Honors and Awards
- *2024* National Scholarship, Xi'an Jiaotong University
- *2024* Fung Scholar and Fung Scholarship, The University of Hong Kong
- *2024* Outstanding Student Cadre, Xi’an Jiaotong University
- *2024* Second Prize, National University Students Electrical Math Modeling Competition
- *2023* Xi'an Jiaotong University First Class Scholarship
- *2023* Outstanding Students Award, Xi'an Jiaotong University
- *2023* Second Prize, National English Competition for College Students
- *2023* Second Prize, FLTRP Uchallenge English Reading Competition


# 📖 Educations
- *2022.09 - Now*, Xi'an Jiaotong University, Bachelor in Software Engineering.
- *2024.09 - 2024.12*, The University of Hong Kong, Exchange Student in Computer Science.

<!-- # 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/) -->

# 💻 Internships
- *2024.04 - Now*, Peking University, Research Internship under the guidance of Prof. Zhouhui Lian at Wangxuan Institute of Computer and Technology.

# 🔍 Research Experience
- Open-ended Financial Competency Assessment
  - Motivations: 
    - Compared to multiple-choice questions, open-ended questions can more authentically and comprehensively reflect the test-takers' proficiency and capabilities.
    - Open-ended questions pose significant challenges in terms of evaluation efficiency and fairness.
    - Financial capability assessment is essential not only for the recruitment of relevant fields, but also for the evaluation of customers' capabilities regarding financial products.
  - Task: Analyze the financial competency of respondents based on their answers to open-ended questions.
  - Ideas:
    - Collect and design representative open-ended questions based on professional knowledge in the financial domain.
    - Evaluate multiple assessment dimensions (financial knowledge, financial behavior, financial consciousness) involved in each sub-question based on Conditional Semantic Textual Similarity (C-STS).
    - Design prompts using prompt engineering techniques such as Chain-of-Thought (CoT), in-context learning (ICL), and role-playing to guide LLMs in generating high-quality datasets.
    - Fine-tune the model using active learning and other strategies.
  - Complete dataset generation and participate in literature investigation.
- An Evaluation System of Survey Result Credibility
  - Motivations:
  	- Evaluating the credibility of survey findings is crucial for research in fields such as Human-Computer Interaction (HCI)
    - Existing methods fall short in assessing the credibility of results from open-ended questionnaires.
  - Task: Evaluate the validity and credibility of survey result data.
  - Ideas: 
    - Break down into four stages including prompt refining, answer generation, answer analysis and credibility assessment. 
    - Assign multiple LLMs of different capabilities and roles to solve sub-problems in each phase.  
    - Integrates the ideas demands of non-technical researchers with the processing procedures of LLMs.
    - Design an intuitive UI to enhance its usability for non-technical researchers.
  - Participate in dataset generation, UI design, and ablation studies.
- Calligraphy Layout Generative Model
  - Motivations:
    - The diverse and flexible layout is one of the major charms of Chinese calligraphy, and the generation of single-character layout is crucial for the overall generation of a calligraphic work. 
    - Using prompt engineering to generate layouts with large language models (LLMs) proved to be less effective and very costly.
  - Task: Generate high-quality layouts for calligraphy generation efficiently.
  - Ideas: 
    - Collected and annotated calligraphy image datasets.
    - Selected base models based on data distribution, performance, and computational efficiency.
    - Fine-tuned multiple models using LoRA, q-LoRA, and compared their performance through visualization.
  - Independently conducted model fine-tuning and visualization. 
- CalliReader: Contextualizing Chinese Calligraphy via an Embedding-Aligned Vision-Language Model   			PKU
  - A versatile vision-language model for Chinese calligraphy contextualization.
  - Model Capability: Full-page/region-wise recognition, multilingual interpretation, and intent analysis.
  - Motivation: Existing Vision-Language Models (VLMs) and OCR methods struggle to achieve satisfactory performance in recognizing Chinese calligraphy and conducting contextual reasoning.
  - Ideas: 
    - Character-wise Slicing: Simplify the recognition task while preserving character semantics.
    - CalliAlign Module: Compress visual tokens and align them with normalized text embeddings.
    - Embedding Instruction Tuning (e-IT): address data scarcity and improve interpretation ability.
    - CalliBench: The first comprehensive benchmark for full-page calligraphic contextualization.
  - Participate in literature investigation, benchmark construction, experiments, and paper writing.
  - Paper link: [https://arxiv.org/pdf/2503.06472](https://arxiv.org/pdf/2503.06472)

# 🖥️ Development Experience
- Multithreaded Optimized Terminal AI Chatbot
  - Objective: Use multithread technique to create an AI chatbot in terminal.
  - Tasks:
    - Different threads to handle tensor calculation in model inference and user interface.
    - Use multiple threads with thread pool to accelerate the calculation of feed forward and attention.
    - Synchronize between different threads using system signal, conditional variables, and semaphores.
    - Analyze the efficiency results with different number of threads and under different scheduling policies.
- PokeFusionLab: Fine-tune a Diffusion Model with Various Datasets, Co-Leader
  - Objective: Customize latent diffusion models using Low-Rank Adaptation (LoRA) to generate images in specific styles and evaluate the impact of different training strategies.
  - Tasks:
    - Fine-tune a diffusion model on a single image to generate stylistically similar images by varying initial Gaussian noise and scaling factors of LoRA matrices.
    - Fine-tune a latent diffusion model on a dataset of Pokémon images with bilingual captions (English and Chinese) to compare the effects of language prompts on image generation.
    - Utilized visual-language models (Qwen2-VL-7b) to re-annotate an image-text dataset with varying levels of detail (brief, middle-brief, detailed captions) and fine-tuned diffusion models using these synthetic texts.
    - Conducted experiments to analyze the impact of detailed annotations on text-to-image generation tasks, showing that more descriptive captions may improve model performance.
- VR Music Firework Show
  - Created an immersive VR experience allowing users to enjoy fireworks with beautiful music across multiple scenic backgrounds.
  - Unity 3D, Google Cardboard SDK
- Sudoku Adventure
  - A Sudoku game with customizable parameters of varying difficulty levels.
  - Java Swing
- Dormitory Management System, Leader
  - A dormitory management system with data panels that allows users to manage with multi-granularity.
  - Vue.js, Spring Boot, MyBatis
- Course Helper of Physics Experiments, Leader
  - An assistant for data processing, analysis, and visualization for physics experiments course in XJTU.
  - WeChat Mini-app (front-end), Python(back-end)

# 🙌 Leadership and Extracurricular Activities
- President, Class No.2227
- Youth League Secretary, Branch No.2202
- Member of XJTU Red Cross
- XJTU Campus Ambassador
- Volunteer Teaching at Pingbian No.1 Middle School in Yunnan Province

# 🏷️ Aditional Information
- English proficiency: IELTS: 7.0; &nbsp; CET4: 603; &nbsp;	CET6: 570
- Interests: Traveling, Sports, Calligraphy, Musicals
