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
- *Mar 2025*: &nbsp; 📝 I am pleased to share that our work, CalliReader, is now available on [arXiv](https://arxiv.org/abs/2503.06472).
- *Dec 2024*: &nbsp; 🌟 Exchange program concluded, but exploration continues!  
- *Sep 2024*: &nbsp; 🎉 Started exchange semester at HKU (The University of Hong Kong)!  
- *Apr 2024*: &nbsp; 🚀 Started research internship in Wangxuan Institute of Computer Technology of PKU guided by Prof. Zhouhui Lian!

# 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Pre-print</div><img src='images/CalliReader500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[CalliReader: Contextualizing Chinese Calligraphy via an Embedding-Aligned Vision-Language Model](https://arxiv.org/pdf/2503.06472)

Yuxuan Luo, Jiaqi Tang, Chenyi Huang, **Feiyang Hao**, Zhouhui Lian

<!-- [**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=DhtAFkwAAAAJ&citation_for_view=DhtAFkwAAAAJ:ALROH1vI_8AC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong> -->
- **Task:** Create a versatile VLM for Chinese calligraphy contextualization ($CC^2$), including full-page/region-wise recognition, multilingual interpretation, and intent analysis.  
- **Ideas:** Proposed character-wise slicing to simplify recognition, introduced the CalliAlign module for embedding alignment, developed Embedding Instruction Tuning (e-IT) to enhance interpretation, and created CalliBench — the first comprehensive benchmark for full-page calligraphic contextualization.  
- **Job:** Conducted a literature review of OCR methods and reasoning benchmarks for VLMs, performed comparisons between our model, state-of-the-art (SOTA) OCR methods, and other competitive VLMs, and participated in benchmark construction, model fine-tuning, ablation study, and paper writing.  
</div>
</div>


# 🎖 Honors and Awards

- *2024* National Scholarship, Xi'an Jiaotong University
- *2024* Fung Scholar and Fung Scholarship, The University of Hong Kong
- *2024* Outstanding Student Cadre, Xi’an Jiaotong University
- *2024* Second Prize, National University Students Electrical Math Modeling Competition
- *2023* Xi'an Jiaotong University First Class Scholarship
- *2023* Outstanding Students Award, Xi'an Jiaotong University
- *2023* Second Prize, National English Competition for College Students
- *2023* Second Prize, FLTRP Uchallenge English Reading Competition


# 📖 Educations and Internships

- *2022.09 - Now*, Xi'an Jiaotong University, Bachelor in Software Engineering.
- *2024.09 - 2024.12*, The University of Hong Kong, Exchange Student in Department of Computer Science. (English Proficiency: IELTS 7.0)
- *2024.04 - Now*, Peking University, Research Internship under the guidance of Prof. Zhouhui Lian at Wangxuan Institute of Computer and Technology.

# 🔍 Experience

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Research Project</div><img src='images/CalliReader500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

Open-ended Financial Competency Assessment

**Keywords:** Conditional Semantic Textual Similarity (C-STS), Prompt Engineering, Active Learning, LLMs  
- **Task:** Develop an LLM-based evaluation framework to address efficiency and fairness challenges in open-ended financial competency assessments for recruitment and customer capability evaluations.  
- **Ideas:** Designed domain-specific open-ended questions and a multi-dimensional C-STS assessment framework, generated high-quality datasets, and optimized model performance using active learning techniques.  
- **Job:** Built a multi-dimensional (knowledge, behavior, awareness) financial QA dataset via Chain of Thought (CoT) / In Context Learning (ICL) / role-playing prompting, and conducted literature reviews.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Research Project</div><img src='images/CalliReader500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

An Evaluation System of Survey Result Credibility

**Keywords:** Post-training, Human-Computer Interaction (HCI), LLMs, UI Design   
- **Task:** Create a phased evaluation system to address credibility gaps in open-ended survey results for HCI research.  
- **Ideas:** Decomposed the process into stages such as prompt refinement, answer generation, analysis, and credibility assessment, leveraging role-specific LLM collaboration and researcher-centric UI design.  
- **Job:** Contributed to dataset development and ablation studies while designing an intuitive user interface that enables non-technical researchers to interact effortlessly with the complex multi-agent system, and implementing with PyQt.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Research Project</div><img src='images/CalliReader500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

Calligraphy Layout Generative Model

**Keywords:** LoRA, q-LoRA, Visualization, Prompt Engineering  
- **Task:** Develop an efficient calligraphy layout generation solution to overcome cost and quality limitations of traditional methods using LLMs and prompt engineering.  
- **Ideas:** Curated a calligraphy image dataset, evaluated baseline methods, and implemented RLHF with visualization-based validation.  
- **Job:** Selected a base model based on data distribution, performance, and computational efficiency, fine-tuned using LoRA/q-LoRA methods and evaluated through visualization techniques, which achieved higher quality results while significantly reducing costs compared to traditional methods.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Development Project</div><img src='images/CalliReader500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

Multithreaded Optimized Terminal AI Chatbot

**Keywords:** Multithreading, Thread Pool, System Signals, Conditional Variables, Semaphores  
- Developed a terminal-based AI chatbot using multithreading techniques, implementing thread pools to accelerate tensor calculations for model inference and using another thread to handle user interface.  
- Synchronized threads using system signals, conditional variables, and semaphores, and analyzed efficiency under varying thread counts and scheduling policies.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Development Project</div><img src='images/CalliReader500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

PokeFusionLab: Fine-tune a Diffusion Model with Various Datasets, Co-Leader

**Keywords:** Latent Diffusion Models, LoRA, Data-Centric AI  
- Fine-tuned latent diffusion models using Low-Rank Adaptation (LoRA) to generate images in specific styles, experimenting with single-image and Pokémon dataset training.  
- Utilized Qwen2-VL-7b to re-annotate datasets with varying caption detail levels, fine-tuning models to analyze the impact of detailed captions on text-to-image generation performance.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Development Project</div><img src='images/CalliReader500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

VR Music Firework Show

**Keywords:** Unity 3D, Google Cardboard SDK  
- Created an immersive VR experience allowing users to enjoy fireworks with beautiful music across multiple scenic backgrounds.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Development Project</div><img src='images/CalliReader500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

Dormitory Management System, Leader

**Keywords:** Vue.js, Spring Boot, MyBatis  
- Developed a dormitory management system with data panels that allows users to manage with multi-granularity.
</div>
</div>

# 🙌 Additional Information

- President, Class No.2227
- Youth League Secretary, Branch No.2202
- Member of XJTU Red Cross
- XJTU Campus Ambassador
- Volunteer Teaching at Pingbian No.1 Middle School in Yunnan Province
- Interests: Traveling, Sports, Calligraphy, Musicals
