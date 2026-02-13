# arXiv AI 论文日报 | 2026-02-13

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (7 篇)
- [cs.LG](#csLG) (14 篇)
- [cs.AI](#csAI) (6 篇)
- [cs.CL](#csCL) (3 篇)

---

## cs.AI

## [1. CM2: Reinforcement Learning with Checklist Rewards for Multi-Turn and Multi-Step Agentic Tool Use](https://arxiv.org/abs/2602.12268v1)

**作者**：Zhen Zhang, Kaiqiang Song, Xun Wang 等 14 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-12

### 📄 论文摘要

AI agents are increasingly used to solve real-world tasks by reasoning over multi-turn user interactions and invoking external tools. However, applying reinforcement learning to such settings remains difficult: realistic objectives often lack verifiable rewards and instead emphasize open-ended behaviors; moreover, RL for multi-turn, multi-step agentic tool use is still underexplored; and building and maintaining executable tool environments is costly, limiting scale and coverage. We propose CM2, an RL framework that replaces verifiable outcome rewards with checklist rewards. CM2 decomposes each turn's intended behavior into fine-grained binary criteria with explicit evidence grounding and structured metadata, turning open-ended judging into more stable classification-style decisions. To balance stability and informativeness, our method adopts a strategy of sparse reward assignment but dense evaluation criteria. Training is performed in a scalable LLM-simulated tool environment, avoiding heavy engineering for large tool sets. Experiments show that CM2 consistently improves over supervised fine-tuning. Starting from an 8B Base model and training on an 8k-example RL dataset, CM2 improves over the SFT counterpart by 8 points on tau^-Bench, by 10 points on BFCL-V4, and by 12 points on ToolSandbox. The results match or even outperform similarly sized open-source baselines, including the judging model. CM2 thus provides a scalable recipe for optimizing multi-turn, multi-step tool-using agents without relying on verifiable rewards. Code provided by the open-source community: https://github.com/namezhenzhang/CM2-RLCR-Tool-Agent.

### 🤖 AI 总结

**一句话总结**：CM2 提出用“检查单式奖励”替代可验证结果奖励，在模拟工具环境中对多轮多步工具型智能体进行强化学习，并显著优于纯监督微调。

**研究动机**：现实多轮工具使用任务目标开放、缺乏可验证奖励，现有 RL 难以稳定训练多步 agent，且真实可执行工具环境昂贵难扩展。

**核心方法**：将每轮期望行为拆解为细粒度二元“检查项”，配有证据和结构化元数据，用稀疏奖励+密集评估标准的策略在 LLM 模拟的工具环境中对 8B 模型进行 RL 训练。

**主要结论**：在 tau^-Bench、BFCL-V4 和 ToolSandbox 等基准上，CM2 相比 SFT 分别提升 8/10/12 分，达到或超越同规模开源基线和评判模型，展示了无需可验证结果奖励即可可扩展地优化多轮多步工具智能体的可行路径。

**关键词**：强化学习, LLM, agenticworkflow, 多轮对话工具调用, 清单式奖励设计, LLM模拟环境, 工具使用策略优化, RLCM2框架

**评分**：65

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12268v1) | [下载PDF](https://arxiv.org/pdf/2602.12268v1.pdf)

---

## [2. Think like a Scientist: Physics-guided LLM Agent for Equation Discovery](https://arxiv.org/abs/2602.12259v1)

**作者**：Jianke Yang, Ohm Venkatachalam, Mohammad Kianezhad 等 5 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-02-12

### 📄 论文摘要

Explaining observed phenomena through symbolic, interpretable formulas is a fundamental goal of science. Recently, large language models (LLMs) have emerged as promising tools for symbolic equation discovery, owing to their broad domain knowledge and strong reasoning capabilities. However, most existing LLM-based systems try to guess equations directly from data, without modeling the multi-step reasoning process that scientists often follow: first inferring physical properties such as symmetries, then using these as priors to restrict the space of candidate equations. We introduce KeplerAgent, an agentic framework that explicitly follows this scientific reasoning process. The agent coordinates physics-based tools to extract intermediate structure and uses these results to configure symbolic regression engines such as PySINDy and PySR, including their function libraries and structural constraints. Across a suite of physical equation benchmarks, KeplerAgent achieves substantially higher symbolic accuracy and greater robustness to noisy data than both LLM and traditional baselines.

### 🤖 AI 总结

**一句话总结**：论文提出KeplerAgent，一个让LLM像物理学家一样先推理物理性质再做符号回归的代理框架，在物理方程发现任务上显著提升准确率和抗噪性。

**研究动机**：现有LLM方程发现方法多直接从数据“猜公式”，忽略科学家常用的分步物理推理流程，导致搜索空间过大、对噪声敏感且缺乏物理约束。

**核心方法**：KeplerAgent用LLM协调一系列物理工具，先从数据中推断对称性等物理结构，再据此配置PySINDy、PySR等符号回归器的函数库和结构约束，实现物理先验引导的公式搜索。

**主要结论**：在多个物理方程基准上，KeplerAgent在符号准确率和噪声鲁棒性上都优于传统符号回归和直接LLM生成方案，表明显式模仿科学推理过程能显著提升方程发现能力。

**关键词**：LLM, 大语言模型, agentic框架, 物理引导符号回归, 方程发现, 科学推理, 多步推理, 物理先验约束, 噪声鲁棒性

**评分**：63

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12259v1) | [下载PDF](https://arxiv.org/pdf/2602.12259v1.pdf)

---

## [3. "Sorry, I Didn't Catch That": How Speech Models Miss What Matters Most](https://arxiv.org/abs/2602.12249v1)

**作者**：Kaitlyn Zhou, Martijn Bartelds, Federico Bianchi 等 4 位作者  
**分类**：cs.AI, cs.CL, cs.CY  
**发布时间**：2026-02-12

### 📄 论文摘要

Despite speech recognition systems achieving low word error rates on standard benchmarks, they often fail on short, high-stakes utterances in real-world deployments. Here, we study this failure mode in a high-stakes task: the transcription of U.S. street names as spoken by U.S. participants. We evaluate 15 models from OpenAI, Deepgram, Google, and Microsoft on recordings from linguistically diverse U.S. speakers and find an average transcription error rate of 44%. We quantify the downstream impact of failed transcriptions by geographic locations and show that mis-transcriptions systematically cause errors for all speakers, but that routing distance errors are twice as large for non-English primary speakers compared to English primary speakers. To mitigate this harm, we introduce a synthetic data generation approach that produces diverse pronunciations of named entities using open-source text-to-speech models. Fine-tuning with less than 1,000 synthetic samples improves street name transcription accuracy by nearly 60% (relative to base models) for non-English primary speakers. Our results highlight a critical gap between benchmark performance and real-world reliability in speech systems and demonstrate a simple, scalable path to reducing high-stakes transcription errors.

### 🤖 AI 总结

**一句话总结**：论文发现当前主流语音识别在真实场景中对街道名等短且高风险语句错误率极高，并提出用少量合成数据微调即可显著改善。

**研究动机**：标准基准上的低词错误率掩盖了真实应用中对关键专有名词（如街道名）和少数族裔/非英语母语者的高失败率，且这些错误会带来严重导航与公平性问题。

**核心方法**：作者采集多语言背景的美国说话人读美国街道名的语音数据，评估四家厂商15个模型的转写表现及其在地理路由上的误差影响，并使用开源TTS合成多样化街道名发音，基于不足1000条合成样本对模型进行微调。

**主要结论**：现有语音模型在街道名转写上的平均错误率高达44%，对非英语母语者造成约两倍的路由距离误差；而通过简单的合成发音数据微调，可将非英语母语者街道名识别准确率相对提升近60%，表明当前基准与真实可靠性存在关键鸿沟且有可扩展的缓解路径。

**关键词**：语音识别, 深度学习, 神经网络, 生成式数据增强, 合成语音数据, 命名实体识别, 多语言口音鲁棒性, 高风险场景转录, rag

**评分**：38

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12249v1) | [下载PDF](https://arxiv.org/pdf/2602.12249v1.pdf)

---

## [4. SAM3-LiteText: An Anatomical Study of the SAM3 Text Encoder for Efficient Vision-Language Segmentation](https://arxiv.org/abs/2602.12173v1)

**作者**：Chengxi Zeng, Yuxuan Jiang, Ge Gao 等 9 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-12

### 📄 论文摘要

Vision-language segmentation models such as SAM3 enable flexible, prompt-driven visual grounding, but inherit large, general-purpose text encoders originally designed for open-ended language understanding. In practice, segmentation prompts are short, structured, and semantically constrained, leading to substantial over-provisioning in text encoder capacity and persistent computational and memory overhead. In this paper, we perform a large-scale anatomical analysis of text prompting in vision-language segmentation, covering 404,796 real prompts across multiple benchmarks. Our analysis reveals severe redundancy: most context windows are underutilized, vocabulary usage is highly sparse, and text embeddings lie on low-dimensional manifold despite high-dimensional representations. Motivated by these findings, we propose SAM3-LiteText, a lightweight text encoding framework that replaces the original SAM3 text encoder with a compact MobileCLIP student that is optimized by knowledge distillation. Extensive experiments on image and video segmentation benchmarks show that SAM3-LiteText reduces text encoder parameters by up to 88%, substantially reducing static memory footprint, while maintaining segmentation performance comparable to the original model. Code: https://github.com/SimonZeng7108/efficientsam3/tree/sam3_litetext.

### 🤖 AI 总结

**一句话总结**：SAM3-LiteText通过分析分割场景中的文本提示冗余，提出用蒸馏得到的小型MobileCLIP文本编码器替换原SAM3文本编码器，在几乎不损失分割精度的前提下大幅降低参数与内存。

**研究动机**：现有如SAM3的视觉-语言分割模型沿用大而通用的文本编码器，但实际分割提示往往短小、结构化且语义空间受限，导致文本编码器严重超配并带来不必要的计算和显存开销。

**核心方法**：作者首先对40万余条真实分割提示进行“解剖式”统计分析，量化上下文窗口利用率、词汇稀疏性和嵌入流形维度等冗余现象；在此基础上设计SAM3-LiteText框架，用更小的MobileCLIP作为学生模型对原SAM3文本编码器进行知识蒸馏，并无缝替换进SAM3以实现高效文本编码。

**主要结论**：实验表明，SAM3-LiteText在多个图像与视频分割基准上几乎保持原有分割性能的同时，将文本编码器参数量最多压缩88%，显著降低静态内存占用，证明针对分割提示定制轻量文本编码器既高效又实用。

**关键词**：深度学习, 神经网络, transformer, 文本编码蒸馏, 轻量级文本编码器, 视觉语言分割, MobileCLIP学生模型, 知识蒸馏训练, 图像分割基准, 视频分割基准

**评分**：30

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12173v1) | [下载PDF](https://arxiv.org/pdf/2602.12173v1.pdf)

---

## [5. Pedagogically-Inspired Data Synthesis for Language Model Knowledge Distillation](https://arxiv.org/abs/2602.12172v1)

**作者**：Bowei He, Yankai Chen, Xiaokun Zhang 等 7 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-02-12

### 📄 论文摘要

Knowledge distillation from Large Language Models (LLMs) to smaller models has emerged as a critical technique for deploying efficient AI systems. However, current methods for distillation via synthetic data lack pedagogical awareness, treating knowledge transfer as a one-off data synthesis and training task rather than a systematic learning process. In this paper, we propose a novel pedagogically-inspired framework for LLM knowledge distillation that draws from fundamental educational principles. Our approach introduces a three-stage pipeline -- Knowledge Identifier, Organizer, and Adapter (IOA) -- that systematically identifies knowledge deficiencies in student models, organizes knowledge delivery through progressive curricula, and adapts representations to match the cognitive capacity of student models. We integrate Bloom's Mastery Learning Principles and Vygotsky's Zone of Proximal Development to create a dynamic distillation process where student models approach teacher model's performance on prerequisite knowledge before advancing, and new knowledge is introduced with controlled, gradual difficulty increments. Extensive experiments using LLaMA-3.1/3.2 and Qwen2.5 as student models demonstrate that IOA achieves significant improvements over baseline distillation methods, with student models retaining 94.7% of teacher performance on DollyEval while using less than 1/10th of the parameters. Our framework particularly excels in complex reasoning tasks, showing 19.2% improvement on MATH and 22.3% on HumanEval compared with state-of-the-art baselines.

### 🤖 AI 总结

**一句话总结**：本文提出一个受教育学启发的三阶段知识蒸馏框架 IOA，通过诊断学生模型薄弱点、设计渐进学习路径并适配难度，使小模型在复杂任务上接近大模型性能。

**研究动机**：现有基于合成数据的蒸馏方法缺乏“教学法”视角，将知识迁移视为一次性数据生成和训练，导致知识传递效率低、对复杂推理能力提升有限。

**核心方法**：框架由知识识别器（识别学生与教师的知识差距）、组织器（基于先修知识与难度递进构建课程）和适配器（将教师输出转换成适合学生认知容量的表示）三部分组成，并结合“掌握学习”和“最近发展区”，动态控制学习顺序与难度升级。

**主要结论**：在 LLaMA-3.1/3.2 和 Qwen2.5 等学生模型上，IOA 在保持不到十分之一参数规模的前提下，在 DollyEval 上保留了 94.7% 的教师性能，并在 MATH 和 HumanEval 等复杂推理任务上分别较现有蒸馏方法提升约 19.2% 和 22.3%。

**关键词**：大语言模型, 知识蒸馏, 合成数据, 教师学生模型, 课程学习, 分阶段训练, 复杂推理能力提升, 教育学启发方法, 模型压缩, 参数高效部署, llm

**评分**：43

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12172v1) | [下载PDF](https://arxiv.org/pdf/2602.12172v1.pdf)

---

## [6. Sci-CoE: Co-evolving Scientific Reasoning LLMs via Geometric Consensus with Sparse Supervision](https://arxiv.org/abs/2602.12164v1)

**作者**：Xiaohan He, Shiyang Feng, Songtao Huang 等 6 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-12

### 📄 论文摘要

Large language models (LLMs) have demonstrated exceptional reasoning capabilities, and co-evolving paradigms have shown promising results in domains such as code and math. However, in scientific reasoning tasks, these models remain fragile due to unreliable solution evaluation and limited diversity in verification strategies. In this work, we propose Sci-CoE, a two-stage scientific co-evolving framework that enables models to self-evolve as both solver and verifier through a transition from sparse supervision to unsupervised learning. In the first stage, the model uses a small set of annotated data to establish fundamental correctness judgment anchors for the Verifier. In the second stage, we introduce a geometric reward mechanism that jointly considers consensus, reliability, and diversity, driving large-scale self-iteration on unlabeled data. Experiments on several general scientific benchmarks demonstrate that Sci-CoE enhances complex reasoning capabilities and exhibits strong scalability, facilitating the construction of more robust and diverse evaluation systems. Codes are available at https://github.com/InternScience/Sci-CoE.

### 🤖 AI 总结

**一句话总结**：Sci-CoE提出一个两阶段“自演化”框架，让同一个LLM同时进化成更强的科学求解器和验证器，在极少标注与大量无标注数据上显著提升科学推理能力。

**研究动机**：现有LLM在科学推理中易出错，主要由于缺乏可靠的自动判分机制和多样化验证策略，导致难以在大规模无标注科学数据上稳定自训练。

**核心方法**：第一阶段用少量标注数据训练Verifier，建立基础正确性判断锚点；第二阶段在大规模无标注数据上，引入同时考虑答案共识度、判断可靠性和解法多样性的几何式奖励机制，驱动求解器与验证器联合自迭代演化。

**主要结论**：在多种通用科学推理基准上，Sci-CoE显著提升复杂推理表现并具备良好扩展性，能构建更鲁棒且多样化的自动评测体系，为科学领域LLM自监督演化提供有效路径。

**关键词**：大语言模型, 科学推理, co-evolving框架, Verifier自博弈, 几何奖励机制, 稀疏监督, 无监督自迭代, 多样性验证策略, 自监督评估系统, llm

**评分**：48

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12164v1) | [下载PDF](https://arxiv.org/pdf/2602.12164v1.pdf)

---

## cs.CL

## [7. ExStrucTiny: A Benchmark for Schema-Variable Structured Information Extraction from Document Images](https://arxiv.org/abs/2602.12203v1)

**作者**：Mathieu Sibue, Andres Muñoz Garza, Samuel Mensah 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-02-12

### 📄 论文摘要

Enterprise documents, such as forms and reports, embed critical information for downstream applications like data archiving, automated workflows, and analytics. Although generalist Vision Language Models (VLMs) perform well on established document understanding benchmarks, their ability to conduct holistic, fine-grained structured extraction across diverse document types and flexible schemas is not well studied. Existing Key Entity Extraction (KEE), Relation Extraction (RE), and Visual Question Answering (VQA) datasets are limited by narrow entity ontologies, simple queries, or homogeneous document types, often overlooking the need for adaptable and structured extraction. To address these gaps, we introduce ExStrucTiny, a new benchmark dataset for structured Information Extraction (IE) from document images, unifying aspects of KEE, RE, and VQA. Built through a novel pipeline combining manual and synthetic human-validated samples, ExStrucTiny covers more varied document types and extraction scenarios. We analyze open and closed VLMs on this benchmark, highlighting challenges such as schema adaptation, query under-specification, and answer localization. We hope our work provides a bedrock for improving generalist models for structured IE in documents.

### 🤖 AI 总结

**一句话总结**：ExStrucTiny 提出一个面向多种文档类型、可变模式(schema-variable)的结构化信息抽取基准，用于系统评测通用视觉语言模型在文档信息抽取上的真实能力。

**研究动机**：现有文档理解数据集多聚焦于固定实体类别、简单问答或单一文档类型，难以反映企业文档中多样且可变的结构化抽取需求，因此需要一个更贴近实际应用、兼顾 KEE/RE/VQA 的统一基准。

**核心方法**：作者设计了一条结合人工标注与合成数据并由人校验的构建管线，生成覆盖多文档类型、多抽取场景的 ExStrucTiny 数据集，将关键实体抽取、关系抽取与视觉问答整合为可变 schema 的结构化信息抽取任务，并在其上系统评测开源与闭源 VLM。

**主要结论**：实验表明当前通用视觉语言模型在模式自适应、在信息不完全定义时的查询理解以及答案在文档中的精确定位等方面仍存在明显挑战，ExStrucTiny 可作为推动面向文档结构化信息抽取的通用模型研究和改进的基础基准。

**关键词**：多模态大模型, 信息抽取, 文档图像理解, 结构化解析, 模式自适应, 问答式标注, 企业文档处理, workflow

**评分**：36

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12203v1) | [下载PDF](https://arxiv.org/pdf/2602.12203v1.pdf)

---

## [8. Visual Reasoning Benchmark: Evaluating Multimodal LLMs on Classroom-Authentic Visual Problems from Primary Education](https://arxiv.org/abs/2602.12196v1)

**作者**：Mohamed Huti, Alasdair Mackintosh, Amy Waldock 等 10 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-02-12

### 📄 论文摘要

AI models have achieved state-of-the-art results in textual reasoning; however, their ability to reason over spatial and relational structures remains a critical bottleneck -- particularly in early-grade maths, which relies heavily on visuals. This paper introduces the visual reasoning benchmark (VRB), a novel dataset designed to evaluate Multimodal Large Language Models (MLLMs) on their ability to solve authentic visual problems from classrooms. This benchmark is built on a set of 701 questions sourced from primary school examinations in Zambia and India, which cover a range of tasks such as reasoning by analogy, pattern completion, and spatial matching. We outline the methodology and development of the benchmark which intentionally uses unedited, minimal-text images to test if models can meet realistic needs of primary education. Our findings reveal a ``jagged frontier'' of capability where models demonstrate better proficiency in static skills such as counting and scaling, but reach a distinct ``spatial ceiling'' when faced with dynamic operations like folding, reflection, and rotation. These weaknesses pose a risk for classroom use on visual reasoning problems, with the potential for incorrect marking, false scaffolding, and reinforcing student misconceptions. Consequently, education-focused benchmarks like the VRB are essential for determining the functional boundaries of multimodal tools used in classrooms.

### 🤖 AI 总结

**一句话总结**：本文构建了一个源自真实小学考试的视觉推理基准 VRB，用于系统评估多模态大模型在课堂真实视觉题目上的能力边界。

**研究动机**：现有多模态模型在文本推理上表现突出，但在小学数学等高度依赖图形、空间和关系推理的真实课堂场景中表现未知且可能存在风险，因此需要一个教育场景原汁原味的视觉推理基准来评估其实际可用性。

**核心方法**：作者从赞比亚和印度的小学考试中收集701道原始视觉题目，涵盖类比推理、模式补全、空间匹配等，多保持最少文字和原始版式，构建VRB基准并系统测试多种MLLM在不同题型上的表现。

**主要结论**：实验发现模型在计数、缩放等静态技能上表现尚可，但在折叠、翻转、旋转等动态空间操作上存在明显“空间天花板”，呈现能力参差的“锯齿边界”，这在真实课堂使用中可能导致错误评分与误导学生，因而强调需要教育专用的基准来划定和理解多模态工具在教学中的功能边界。

**关键词**：多模态大模型, 视觉推理, 神经网络, transformer, 小学数学教育, 空间关系理解, 图像题自动评分, 教育评测基准

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12196v1) | [下载PDF](https://arxiv.org/pdf/2602.12196v1.pdf)

---

## [9. Query-focused and Memory-aware Reranker for Long Context Processing](https://arxiv.org/abs/2602.12192v1)

**作者**：Yuqing Li, Jiangnan Li, Mo Yu 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-02-12

### 📄 论文摘要

Built upon the existing analysis of retrieval heads in large language models, we propose an alternative reranking framework that trains models to estimate passage-query relevance using the attention scores of selected heads. This approach provides a listwise solution that leverages holistic information within the entire candidate shortlist during ranking. At the same time, it naturally produces continuous relevance scores, enabling training on arbitrary retrieval datasets without requiring Likert-scale supervision. Our framework is lightweight and effective, requiring only small-scale models (e.g., 4B parameters) to achieve strong performance. Extensive experiments demonstrate that our method outperforms existing state-of-the-art pointwise and listwise rerankers across multiple domains, including Wikipedia and long narrative datasets. It further establishes a new state-of-the-art on the LoCoMo benchmark that assesses the capabilities of dialogue understanding and memory usage. We further demonstrate that our framework supports flexible extensions. For example, augmenting candidate passages with contextual information further improves ranking accuracy, while training attention heads from middle layers enhances efficiency without sacrificing performance.

### 🤖 AI 总结

**一句话总结**：提出一种利用大模型检索注意力头、面向查询且具记忆感知的列表式重排框架，在长上下文任务上超过现有点式和列式重排器。

**研究动机**：现有重排器难以高效利用长上下文中的整体候选列表信息，且常依赖人工Likert标注、模型规模大和对长对话记忆的处理不足。

**核心方法**：从选定注意力头中提取passage-query注意力分数，构建能够输出连续相关度的列表式重排模型；在4B规模模型上训练，并可扩展为加入上下文增强候选片段或使用中层注意力头以提高效率。

**主要结论**：该方法在Wikipedia、长叙事数据集和LoCoMo长对话记忆基准上均取得SOTA表现，在保持模型轻量的同时提升长上下文理解与记忆利用能力，并展示出良好的可扩展性和效率。

**关键词**：大语言模型, 深度学习, 检索增强生成, 长上下文处理, 注意力头重排序, 查询相关性建模, 对话记忆理解, LoCoMo基准测试, rag

**评分**：40

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12192v1) | [下载PDF](https://arxiv.org/pdf/2602.12192v1.pdf)

---

## cs.CV

## [10. Stroke of Surprise: Progressive Semantic Illusions in Vector Sketching](https://arxiv.org/abs/2602.12280v1)

**作者**：Huai-Hsun Cheng, Siang-Ling Zhang, Yu-Lun Liu  
**分类**：cs.CV  
**发布时间**：2026-02-12

### 📄 论文摘要

Visual illusions traditionally rely on spatial manipulations such as multi-view consistency. In this work, we introduce Progressive Semantic Illusions, a novel vector sketching task where a single sketch undergoes a dramatic semantic transformation through the sequential addition of strokes. We present Stroke of Surprise, a generative framework that optimizes vector strokes to satisfy distinct semantic interpretations at different drawing stages. The core challenge lies in the "dual-constraint": initial prefix strokes must form a coherent object (e.g., a duck) while simultaneously serving as the structural foundation for a second concept (e.g., a sheep) upon adding delta strokes. To address this, we propose a sequence-aware joint optimization framework driven by a dual-branch Score Distillation Sampling (SDS) mechanism. Unlike sequential approaches that freeze the initial state, our method dynamically adjusts prefix strokes to discover a "common structural subspace" valid for both targets. Furthermore, we introduce a novel Overlay Loss that enforces spatial complementarity, ensuring structural integration rather than occlusion. Extensive experiments demonstrate that our method significantly outperforms state-of-the-art baselines in recognizability and illusion strength, successfully expanding visual anagrams from the spatial to the temporal dimension. Project page: https://stroke-of-surprise.github.io/

### 🤖 AI 总结

**一句话总结**：论文提出一种在矢量素描中，通过逐步添加笔画让同一图像在不同阶段呈现截然不同语义（如从鸭到羊）的生成框架。

**研究动机**：现有视觉错觉多依赖空间布局与多视角，而缺乏在“随时间绘制过程”中实现语义错位与渐进式视觉双关的系统方法，因此作者希望在矢量草图领域构建可控的“时间维度视觉字谜”。

**核心方法**：提出 Stroke of Surprise 框架，将草图笔画建模为可优化的矢量序列，设计双分支的 Score Distillation Sampling 对前缀目标和最终目标同时施加约束，并通过序列感知的联合优化动态调整前缀笔画以寻找两种语义的公共结构子空间，同时引入 Overlay Loss 保证新增笔画与已有结构是互补融合而非遮挡。

**主要结论**：实验表明该方法在草图可识别度和“语义错觉强度”上显著优于现有基线，成功将视觉变位字的概念从纯空间扩展到时间维度的绘制过程，为生成式绘画与交互式视觉表达提供了新的范式。

**关键词**：生成式模型, 深度学习, 扩散模型, ScoreDistillationSampling, 向量素描, 渐进式语义错觉, 双分支联合优化, 结构子空间, OverlayLoss, 视觉幻觉生成, generative

**评分**：20

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12280v1) | [下载PDF](https://arxiv.org/pdf/2602.12280v1.pdf)

---

## [11. UniT: Unified Multimodal Chain-of-Thought Test-time Scaling](https://arxiv.org/abs/2602.12279v1)

**作者**：Leon Liangyu Chen, Haoyu Ma, Zhipeng Fan 等 14 位作者  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-02-12

### 📄 论文摘要

Unified models can handle both multimodal understanding and generation within a single architecture, yet they typically operate in a single pass without iteratively refining their outputs. Many multimodal tasks, especially those involving complex spatial compositions, multiple interacting objects, or evolving instructions, require decomposing instructions, verifying intermediate results, and making iterative corrections. While test-time scaling (TTS) has demonstrated that allocating additional inference compute for iterative reasoning substantially improves language model performance, extending this paradigm to unified multimodal models remains an open challenge. We introduce UniT, a framework for multimodal chain-of-thought test-time scaling that enables a single unified model to reason, verify, and refine across multiple rounds. UniT combines agentic data synthesis, unified model training, and flexible test-time inference to elicit cognitive behaviors including verification, subgoal decomposition, and content memory. Our key findings are: (1) unified models trained on short reasoning trajectories generalize to longer inference chains at test time; (2) sequential chain-of-thought reasoning provides a more scalable and compute-efficient TTS strategy than parallel sampling; (3) training on generation and editing trajectories improves out-of-distribution visual reasoning. These results establish multimodal test-time scaling as an effective paradigm for advancing both generation and understanding in unified models.

### 🤖 AI 总结

**一句话总结**：UniT 提出一种统一多模态模型的链式思维测试时扩展框架，让同一模型在推理过程中迭代生成、验证与修正多轮输出。

**研究动机**：现有统一多模态模型多为单次前向推理，难以应对复杂空间关系、多物体交互和动态指令等需要分解与逐步校验的任务，且测试时扩展在多模态统一模型上仍未被系统探索。

**核心方法**：UniT 通过构建带有推理与编辑轨迹的代理式数据、训练单一统一多模态模型同时支持理解与生成，并在测试阶段采用多轮顺序链式推理与验证机制，实现分解子目标、内容记忆和自我校正。

**主要结论**：实验表明：统一模型在短推理轨迹上训练即可在测试时泛化到更长推理链；顺序链式推理相比并行采样更具计算效率和可扩展性；加入生成与编辑轨迹训练显著提升了分布外视觉推理能力，从而验证了多模态测试时扩展作为统一模型提升范式的有效性。

**关键词**：多模态大模型, chain-of-thought推理, test-time scaling, agentic数据合成, 统一模型训练, 迭代推理, 视觉推理, 内容记忆

**评分**：43

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12279v1) | [下载PDF](https://arxiv.org/pdf/2602.12279v1.pdf)

---

## [12. MonarchRT: Efficient Attention for Real-Time Video Generation](https://arxiv.org/abs/2602.12271v1)

**作者**：Krish Agarwal, Zhuoming Chen, Cheng Luo 等 8 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-02-12

### 📄 论文摘要

Real-time video generation with Diffusion Transformers is bottlenecked by the quadratic cost of 3D self-attention, especially in real-time regimes that are both few-step and autoregressive, where errors compound across time and each denoising step must carry substantially more information. In this setting, we find that prior sparse-attention approximations break down, despite showing strong results for bidirectional, many-step diffusion. Specifically, we observe that video attention is not reliably sparse, but instead combines pronounced periodic structure driven by spatiotemporal position with dynamic, sparse semantic correspondences and dense mixing, exceeding the representational capacity of even oracle top-k attention. Building on this insight, we propose Monarch-RT, a structured attention parameterization for video diffusion models that factorizes attention using Monarch matrices. Through appropriately aligned block structure and our extended tiled Monarch parameterization, we achieve high expressivity while preserving computational efficiency. We further overcome the overhead of parameterization through finetuning, with custom Triton kernels. We first validate the high efficacy of Monarch-RT over existing sparse baselines designed only for bidirectional models. We further observe that Monarch-RT attains up to 95% attention sparsity with no loss in quality when applied to the state-of-the-art model Self-Forcing, making Monarch-RT a pioneering work on highly-capable sparse attention parameterization for real-time video generation. Our optimized implementation outperforms FlashAttention-2, FlashAttention-3, and FlashAttention-4 kernels on Nvidia RTX 5090, H100, and B200 GPUs respectively, providing kernel speedups in the range of 1.4-11.8X. This enables us, for the first time, to achieve true real-time video generation with Self-Forcing at 16 FPS on a single RTX 5090.

### 🤖 AI 总结

**一句话总结**：MonarchRT 提出一种基于 Monarch 矩阵的高效注意力参数化，使实时扩散 Transformer 视频生成在保持质量的同时实现高稀疏度和大幅提速。

**研究动机**：3D 自注意力在少步、自动回归的实时视频扩散模型中计算代价呈二次增长，且传统稀疏注意力在此场景下失效，因为视频注意力既有周期性结构又包含动态稀疏语义和致密混合，难以用简单 top-k 稀疏近似。

**核心方法**：作者分析视频注意力结构特性后，引入 Monarch-RT：将注意力用 Monarch 矩阵进行分块因式分解，并通过对齐块结构与扩展 tiled Monarch 参数化提升表达力，同时配合 Triton 自定义算子与微调以消除额外开销。

**主要结论**：Monarch-RT 相比现有为双向扩散设计的稀疏注意力基线效果更优，在 SOTA 模型 Self-Forcing 中可实现高达 95% 注意力稀疏度而无质量损失，并在 RTX 5090、H100、B200 上相较 FlashAttention-2/3/4 获得 1.4–11.8 倍 kernel 加速，使单张 RTX 5090 上以 16 FPS 实现真正实时视频生成成为可能。

**关键词**：扩散模型, DiffusionTransformer, Transformer, 稀疏注意力, 视频生成, 实时生成, Monarch矩阵, 自注意力加速, 显存优化, 高帧率推理

**评分**：40

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12271v1) | [下载PDF](https://arxiv.org/pdf/2602.12271v1.pdf)

---

## [13. Best of Both Worlds: Multimodal Reasoning and Generation via Unified Discrete Flow Matching](https://arxiv.org/abs/2602.12221v1)

**作者**：Onkar Susladkar, Tushar Prakash, Gayatri Deshmukh 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-12

### 📄 论文摘要

We propose UniDFlow, a unified discrete flow-matching framework for multimodal understanding, generation, and editing. It decouples understanding and generation via task-specific low-rank adapters, avoiding objective interference and representation entanglement, while a novel reference-based multimodal preference alignment optimizes relative outcomes under identical conditioning, improving faithfulness and controllability without large-scale retraining. UniDFlpw achieves SOTA performance across eight benchmarks and exhibits strong zero-shot generalization to tasks including inpainting, in-context image generation, reference-based editing, and compositional generation, despite no explicit task-specific training.

### 🤖 AI 总结

**一句话总结**：UniDFlow 提出一个统一的离散流匹配框架，通过解耦理解与生成并结合参考式偏好对齐，在多模态理解与生成任务上实现高性能与强泛化。

**研究动机**：现有多模态模型在理解和生成目标上常出现优化目标冲突与表示耦合，同时缺乏在多种编辑/控制任务上的统一泛化能力，且提高可控性与忠实度往往需要大规模重训练。

**核心方法**：方法上使用统一的离散 flow-matching 作为生成骨干，通过任务特定的低秩适配器分别优化理解与生成以避免目标干扰，并引入基于参考结果的多模态偏好对齐，在相同条件下对不同输出进行相对比较优化，提高生成的忠实度和可控性。

**主要结论**：UniDFlow 在八个基准上取得 SOTA 表现，并在图像修补、上下文图像生成、参考式编辑与组合生成等未显式训练任务上展现出强零样本泛化能力，证明了统一离散流框架与参考式偏好对齐在多模态理解与生成上的有效性。

**关键词**：深度学习, 多模态推理, 多模态生成, 离散流匹配, 低秩适配器, 多模态偏好对齐, 参考引导编辑, RAG

**评分**：42

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12221v1) | [下载PDF](https://arxiv.org/pdf/2602.12221v1.pdf)

---

## [14. DreamID-Omni: Unified Framework for Controllable Human-Centric Audio-Video Generation](https://arxiv.org/abs/2602.12160v1)

**作者**：Xu Guo, Fulong Ye, Qichao Sun 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-12

### 📄 论文摘要

Recent advancements in foundation models have revolutionized joint audio-video generation. However, existing approaches typically treat human-centric tasks including reference-based audio-video generation (R2AV), video editing (RV2AV) and audio-driven video animation (RA2V) as isolated objectives. Furthermore, achieving precise, disentangled control over multiple character identities and voice timbres within a single framework remains an open challenge. In this paper, we propose DreamID-Omni, a unified framework for controllable human-centric audio-video generation. Specifically, we design a Symmetric Conditional Diffusion Transformer that integrates heterogeneous conditioning signals via a symmetric conditional injection scheme. To resolve the pervasive identity-timbre binding failures and speaker confusion in multi-person scenarios, we introduce a Dual-Level Disentanglement strategy: Synchronized RoPE at the signal level to ensure rigid attention-space binding, and Structured Captions at the semantic level to establish explicit attribute-subject mappings. Furthermore, we devise a Multi-Task Progressive Training scheme that leverages weakly-constrained generative priors to regularize strongly-constrained tasks, preventing overfitting and harmonizing disparate objectives. Extensive experiments demonstrate that DreamID-Omni achieves comprehensive state-of-the-art performance across video, audio, and audio-visual consistency, even outperforming leading proprietary commercial models. We will release our code to bridge the gap between academic research and commercial-grade applications.

### 🤖 AI 总结

**一句话总结**：DreamID-Omni 提出一个统一框架，实现多人物、多声线的人体中心可控音视频生成与编辑，并在多任务上取得 SOTA 表现。

**研究动机**：现有方法把参考生成、视频编辑和音频驱动动画视为割裂任务，且难以在单一模型中实现多角色身份和声纹的精细解耦与控制，因此需要一个统一且可控的音视频生成框架。

**核心方法**：提出对多模态条件对称注入的 Symmetric Conditional Diffusion Transformer，并通过信号级的 Synchronized RoPE 和语义级的 Structured Captions 实现身份-声纹双层解耦，再结合多任务渐进训练，用弱约束生成先验去正则强约束任务、防止过拟合。

**主要结论**：实验表明 DreamID-Omni 在视频质量、音频质量及视听一致性上全面优于现有学术与商业系统，实现统一框架下的人体中心音视频生成与编辑，具备实际落地潜力，代码将开源以促进研究与应用。

**关键词**：深度学习, 扩散模型, Transformer, 生成式音视频, 多人物身份控制, 语音音色解耦, 条件生成框架, 多任务渐进训练, 人类中心视频生成

**评分**：40

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12160v1) | [下载PDF](https://arxiv.org/pdf/2602.12160v1.pdf)

---

## [15. TexSpot: 3D Texture Enhancement with Spatially-uniform Point Latent Representation](https://arxiv.org/abs/2602.12157v1)

**作者**：Ziteng Lu, Yushuang Wu, Chongjie Ye 等 10 位作者  
**分类**：cs.CV, cs.GR  
**发布时间**：2026-02-12

### 📄 论文摘要

High-quality 3D texture generation remains a fundamental challenge due to the view-inconsistency inherent in current mainstream multi-view diffusion pipelines. Existing representations either rely on UV maps, which suffer from distortion during unwrapping, or point-based methods, which tightly couple texture fidelity to geometric density that limits high-resolution texture generation. To address these limitations, we introduce TexSpot, a diffusion-based texture enhancement framework. At its core is Texlet, a novel 3D texture representation that merges the geometric expressiveness of point-based 3D textures with the compactness of UV-based representation. Each Texlet latent vector encodes a local texture patch via a 2D encoder and is further aggregated using a 3D encoder to incorporate global shape context. A cascaded 3D-to-2D decoder reconstructs high-quality texture patches, enabling the Texlet space learning. Leveraging this representation, we train a diffusion transformer conditioned on Texlets to refine and enhance textures produced by multi-view diffusion methods. Extensive experiments demonstrate that TexSpot significantly improves visual fidelity, geometric consistency, and robustness over existing state-of-the-art 3D texture generation and enhancement approaches. Project page: https://anonymous.4open.science/w/TexSpot-page-2D91.

### 🤖 AI 总结

**一句话总结**：TexSpot提出一种名为Texlet的点潜表示，并结合扩散Transformer对现有多视角方法生成的3D纹理进行一致性增强与细节提升。

**研究动机**：现有3D纹理生成要么依赖存在展开畸变的UV贴图，要么依赖强绑定几何密度的点基表示，导致视角不一致和难以生成高分辨率纹理，因此需要一种既表达力强又紧凑、且与几何解耦的3D纹理表示。

**核心方法**：提出Texlet：用2D编码器将局部纹理块编码为点潜向量，再用3D编码器聚合全局几何上下文，并通过级联3D到2D解码器重建高质量纹理块，在此表示上训练条件扩散Transformer，对多视角扩散生成的初始纹理进行统一精修与增强。

**主要结论**：实验表明TexSpot在视觉质量、几何与视角一致性以及鲁棒性上均显著优于现有3D纹理生成与增强方法，验证了Texlet表示与扩散增强框架在高质量3D纹理生成上的有效性。

**关键词**：扩散模型, transformer, 生成式纹理增强, 3D纹理生成, 点云表示, UV贴图融合, 多视角一致性

**评分**：30

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12157v1) | [下载PDF](https://arxiv.org/pdf/2602.12157v1.pdf)

---

## [16. FAIL: Flow Matching Adversarial Imitation Learning for Image Generation](https://arxiv.org/abs/2602.12155v1)

**作者**：Yeyao Ma, Chen Li, Xiaosong Zhang 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-12

### 📄 论文摘要

Post-training of flow matching models-aligning the output distribution with a high-quality target-is mathematically equivalent to imitation learning. While Supervised Fine-Tuning mimics expert demonstrations effectively, it cannot correct policy drift in unseen states. Preference optimization methods address this but require costly preference pairs or reward modeling. We propose Flow Matching Adversarial Imitation Learning (FAIL), which minimizes policy-expert divergence through adversarial training without explicit rewards or pairwise comparisons. We derive two algorithms: FAIL-PD exploits differentiable ODE solvers for low-variance pathwise gradients, while FAIL-PG provides a black-box alternative for discrete or computationally constrained settings. Fine-tuning FLUX with only 13,000 demonstrations from Nano Banana pro, FAIL achieves competitive performance on prompt following and aesthetic benchmarks. Furthermore, the framework generalizes effectively to discrete image and video generation, and functions as a robust regularizer to mitigate reward hacking in reward-based optimization. Code and data are available at https://github.com/HansPolo113/FAIL.

### 🤖 AI 总结

**一句话总结**：本文提出将流匹配图像生成模型的后训练形式化为模仿学习，并用对抗式模仿学习框架 FAIL 替代偏好优化，在少量示例下大幅提升图像生成质量与对齐能力。

**研究动机**：现有基于流匹配的生成模型后训练多依赖监督微调或偏好优化：前者无法纠正未见状态下的策略漂移，后者又需要昂贵的偏好标注或奖励建模，因此需要一种无需显式奖励、但能直接最小化策略与专家分布差异的高效方法。

**核心方法**：作者将流匹配后训练视为模仿学习问题，引入对抗式训练来估计并最小化生成策略与专家分布的差异，提出两种算法：FAIL-PD 利用可微分 ODE 求解器进行低方差路径梯度优化，FAIL-PG 则以黑盒策略梯度方式支持离散或算力受限场景，并在图像/视频生成中统一应用。

**主要结论**：在仅使用约 1.3 万条 Nano Banana pro 示范的条件下，对 FLUX 进行 FAIL 微调即可在指令跟随与美学指标上达到有竞争力甚至更优表现；该框架可推广到离散图像和视频生成，并在奖励优化场景中充当稳定正则项，有效缓解 reward hacking 问题。

**关键词**：深度学习, 生成式模型, flow matching, 对抗式模仿学习, 扩散模型, 图像生成, 视频生成, 策略优化, 奖励黑客防护, reward model

**评分**：40

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12155v1) | [下载PDF](https://arxiv.org/pdf/2602.12155v1.pdf)

---

## cs.LG

## [17. Function-Space Decoupled Diffusion for Forward and Inverse Modeling in Carbon Capture and Storage](https://arxiv.org/abs/2602.12274v1)

**作者**：Xin Ju, Jiachen Yao, Anima Anandkumar 等 5 位作者  
**分类**：cs.LG, physics.geo-ph  
**发布时间**：2026-02-12

### 📄 论文摘要

Accurate characterization of subsurface flow is critical for Carbon Capture and Storage (CCS) but remains challenged by the ill-posed nature of inverse problems with sparse observations. We present Fun-DDPS, a generative framework that combines function-space diffusion models with differentiable neural operator surrogates for both forward and inverse modeling. Our approach learns a prior distribution over geological parameters (geomodel) using a single-channel diffusion model, then leverages a Local Neural Operator (LNO) surrogate to provide physics-consistent guidance for cross-field conditioning on the dynamics field. This decoupling allows the diffusion prior to robustly recover missing information in parameter space, while the surrogate provides efficient gradient-based guidance for data assimilation. We demonstrate Fun-DDPS on synthetic CCS modeling datasets, achieving two key results: (1) For forward modeling with only 25% observations, Fun-DDPS achieves 7.7% relative error compared to 86.9% for standard surrogates (an 11x improvement), proving its capability to handle extreme data sparsity where deterministic methods fail. (2) We provide the first rigorous validation of diffusion-based inverse solvers against asymptotically exact Rejection Sampling (RS) posteriors. Both Fun-DDPS and the joint-state baseline (Fun-DPS) achieve Jensen-Shannon divergence less than 0.06 against the ground truth. Crucially, Fun-DDPS produces physically consistent realizations free from the high-frequency artifacts observed in joint-state baselines, achieving this with 4x improved sample efficiency compared to rejection sampling.

### 🤖 AI 总结

**一句话总结**：本文提出Fun-DDPS框架，将函数空间扩散模型与可微分神经算子解耦结合，实现对CCS地下流动的高精度前向与反演建模，尤其在观测极度稀疏场景下表现显著优于传统方法。

**研究动机**：CCS场景中地下流动的参数反演问题高度病态且观测稀疏，传统确定性/代理模型在缺失信息和不确定性表征方面表现不佳，因此需要同时能表达先验分布、利用物理规律并支持高效贝叶斯反演的生成式方法。

**核心方法**：方法先用单通道函数空间扩散模型学习地质参数（geomodel）的先验分布，再用局部神经算子LNO作为物理一致的可微代理，对动力学场进行跨场条件与梯度引导，从而实现“先验生成 + 物理解耦指导”的前向与反演联合建模。

**主要结论**：在合成CCS数据上，Fun-DDPS在仅有25%观测的前向预测中将相对误差从传统代理的86.9%降至7.7%，并在反演任务中与近似精确的拒绝采样后验相比JSD<0.06，且样本效率提升约4倍并避免联合建模基线中出现的高频伪影，证明了该解耦扩散框架在极端稀疏观测与物理一致性上的优势。

**关键词**：生成式扩散模型, 深度学习, 神经算子, 物理引导建模, 函数空间建模, 碳捕集与封存, 地质参数反演, 稀疏观测数据同化, 前向建模, 逆问题求解, generative

**评分**：26

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12274v1) | [下载PDF](https://arxiv.org/pdf/2602.12274v1.pdf)

---

## [18. Self-Supervised Learning via Flow-Guided Neural Operator on Time-Series Data](https://arxiv.org/abs/2602.12267v1)

**作者**：Duy Nguyen, Jiachen Yao, Jiayun Wang 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-12

### 📄 论文摘要

Self-supervised learning (SSL) is a powerful paradigm for learning from unlabeled time-series data. However, popular methods such as masked autoencoders (MAEs) rely on reconstructing inputs from a fixed, predetermined masking ratio. Instead of this static design, we propose treating the corruption level as a new degree of freedom for representation learning, enhancing flexibility and performance. To achieve this, we introduce the Flow-Guided Neural Operator (FGNO), a novel framework combining operator learning with flow matching for SSL training. FGNO learns mappings in functional spaces by using Short-Time Fourier Transform to unify different time resolutions. We extract a rich hierarchy of features by tapping into different network layers and flow times that apply varying strengths of noise to the input data. This enables the extraction of versatile representations, from low-level patterns to high-level global features, using a single model adaptable to specific tasks. Unlike prior generative SSL methods that use noisy inputs during inference, we propose using clean inputs for representation extraction while learning representations with noise; this eliminates randomness and boosts accuracy. We evaluate FGNO across three biomedical domains, where it consistently outperforms established baselines. Our method yields up to 35% AUROC gains in neural signal decoding (BrainTreeBank), 16% RMSE reductions in skin temperature prediction (DREAMT), and over 20% improvement in accuracy and macro-F1 on SleepEDF under low-data regimes. These results highlight FGNO's robustness to data scarcity and its superior capacity to learn expressive representations for diverse time series.

### 🤖 AI 总结

**一句话总结**：论文提出一种基于流匹配与神经算子的新型自监督框架FGNO，通过在函数空间中学习不同腐蚀强度下的时间序列表征，显著提升多种生物医学时间序列任务效果。

**研究动机**：现有时间序列自监督方法多采用固定掩码或固定噪声策略，缺乏对“腐蚀强度”这一新自由度的系统利用，难以在低数据场景下学到既细粒度又全局的通用表征。

**核心方法**：FGNO使用短时傅里叶变换将不同时间分辨率统一到函数空间，结合流匹配学习从噪声到干净信号的映射，并从不同网络层和不同流时间（对应不同噪声强度）提取多层次特征；训练时通过噪声腐蚀进行自监督学习，推理时仅用干净输入提取稳定表征。

**主要结论**：在神经信号解码、皮肤温度预测和睡眠阶段分类等三个生物医学基准上，FGNO在AUROC、RMSE、准确率和macro-F1等指标上显著优于主流基线，展现出对数据稀缺和多任务场景的强鲁棒性和表征能力。

**关键词**：自监督学习, 深度学习, 神经网络, 时间序列表示学习, 流匹配模型, NeuralOperator, 频域特征提取, 生物医学信号分析, 无监督预训练, generative

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12267v1) | [下载PDF](https://arxiv.org/pdf/2602.12267v1.pdf)

---

## [19. Community Concealment from Unsupervised Graph Learning-Based Clustering](https://arxiv.org/abs/2602.12250v1)

**作者**：Dalyapraz Manatova, Pablo Moriano, L. Jean Camp  
**分类**：cs.LG, cs.CR, cs.SI  
**发布时间**：2026-02-12

### 📄 论文摘要

Graph neural networks (GNNs) are designed to use attributed graphs to learn representations. Such representations are beneficial in the unsupervised learning of clusters and community detection. Nonetheless, such inference may reveal sensitive groups, clustered systems, or collective behaviors, raising concerns regarding group-level privacy. Community attribution in social and critical infrastructure networks, for example, can expose coordinated asset groups, operational hierarchies, and system dependencies that could be used for profiling or intelligence gathering. We study a defensive setting in which a data publisher (defender) seeks to conceal a community of interest while making limited, utility-aware changes in the network. Our analysis indicates that community concealment is strongly influenced by two quantifiable factors: connectivity at the community boundary and feature similarity between the protected community and adjacent communities. Informed by these findings, we present a perturbation strategy that rewires a set of selected edges and modifies node features to reduce the distinctiveness leveraged by GNN message passing. The proposed method outperforms DICE in our experiments on synthetic benchmarks and real network graphs under identical perturbation budgets. Overall, it achieves median relative concealment improvements of approximately 20-45% across the evaluated settings. These findings demonstrate a mitigation strategy against GNN-based community learning and highlight group-level privacy risks intrinsic to graph learning.

### 🤖 AI 总结

**一句话总结**：本文研究如何在有限扰动预算下，通过修改图结构和节点特征来隐蔽特定社区，使基于GNN的无监督聚类/社区检测难以识别该社区。

**研究动机**：GNN在无监督社区检测中表现优异，但会暴露敏感群体和系统结构，带来群体层面的隐私与安全风险，因此需要面向“数据发布者”的防御机制来隐藏特定社区。

**核心方法**：作者分析影响社区隐蔽性的两个关键因素——社区边界连通性与与邻接社区的特征相似度，并据此设计了一种在扰动预算下重连部分边和修改节点特征的策略，以削弱GNN消息传递所依赖的区分性信息。

**主要结论**：在合成与真实网络上，该方法在相同扰动预算下相较DICE可带来约20–45%的中位相对隐蔽性提升，说明有可能通过有针对性的图扰动有效对抗基于GNN的社区学习，同时揭示了图学习固有的群体隐私风险。

**关键词**：图神经网络, 无监督学习, 社区检测, 图表示学习, 隐私保护, 对抗扰动, 边重连, 特征扰动, 社交网络安全, neural network

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12250v1) | [下载PDF](https://arxiv.org/pdf/2602.12250v1.pdf)

---

## [20. ExtractBench: A Benchmark and Evaluation Methodology for Complex Structured Extraction](https://arxiv.org/abs/2602.12247v1)

**作者**：Nick Ferguson, Josh Pennington, Narek Beghian 等 7 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-12

### 📄 论文摘要

Unstructured documents like PDFs contain valuable structured information, but downstream systems require this data in reliable, standardized formats. LLMs are increasingly deployed to automate this extraction, making accuracy and reliability paramount. However, progress is bottlenecked by two gaps. First, no end-to-end benchmark evaluates PDF-to-JSON extraction under enterprise-scale schema breadth. Second, no principled methodology captures the semantics of nested extraction, where fields demand different notions of correctness (exact match for identifiers, tolerance for quantities, semantic equivalence for names), arrays require alignment, and omission must be distinguished from hallucination. We address both gaps with ExtractBench, an open-source benchmark and evaluation framework for PDF-to-JSON structured extraction. The benchmark pairs 35 PDF documents with JSON Schemas and human-annotated gold labels across economically valuable domains, yielding 12,867 evaluatable fields spanning schema complexities from tens to hundreds of fields. The evaluation framework treats the schema as an executable specification: each field declares its scoring metric. Baseline evaluations reveal that frontier models (GPT-5/5.2, Gemini-3 Flash/Pro, Claude 4.5 Opus/Sonnet) remain unreliable on realistic schemas. Performance degrades sharply with schema breadth, culminating in 0% valid output on a 369-field financial reporting schema across all tested models. We release ExtractBench at https://github.com/ContextualAI/extract-bench.

### 🤖 AI 总结

**一句话总结**：ExtractBench 提出首个面向复杂企业级 JSON Schema 的 PDF→JSON 结构化抽取基准和可执行评测框架，并显示当前前沿 LLM 在此任务上仍然很不可靠。

**研究动机**：现有工作缺乏同时覆盖大规模、多层级 JSON Schema 的端到端 PDF 抽取基准，也缺乏能区分不同字段语义正确性（精确匹配、数值容差、语义等价）、数组对齐及缺失与幻觉的系统化评估方法。

**核心方法**：构建包含35个 PDF 文档、配套 JSON Schema 与人工标注金标的公开基准，覆盖12,867个可评估字段，并将 schema 视为“可执行规范”，在每个字段中声明具体评分指标以自动评测复杂嵌套与数组结构的抽取质量。

**主要结论**：在 ExtractBench 上，GPT-5、Gemini-3、Claude 4.5 等前沿 LLM 在真实复杂 Schema 上表现不稳定，随字段规模扩大性能急剧下降，在包含369字段的财报 Schema 上所有模型的有效输出率甚至降为 0%，表明当前 LLM 仍难以可靠胜任企业级复杂结构抽取。

**关键词**：大模型, 结构化信息抽取, PDF文档解析, JSON模式对齐, 嵌套字段评估, 企业级信息抽取基准, 开放源代码评测框架, llm

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12247v1) | [下载PDF](https://arxiv.org/pdf/2602.12247v1.pdf)

---

## [21. Intrinsic-Energy Joint Embedding Predictive Architectures Induce Quasimetric Spaces](https://arxiv.org/abs/2602.12245v1)

**作者**：Anthony Kobanda, Waris Radji  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-12

### 📄 论文摘要

Joint-Embedding Predictive Architectures (JEPAs) aim to learn representations by predicting target embeddings from context embeddings, inducing a scalar compatibility energy in a latent space. In contrast, Quasimetric Reinforcement Learning (QRL) studies goal-conditioned control through directed distance values (cost-to-go) that support reaching goals under asymmetric dynamics. In this short article, we connect these viewpoints by restricting attention to a principled class of JEPA energy functions : intrinsic (least-action) energies, defined as infima of accumulated local effort over admissible trajectories between two states. Under mild closure and additivity assumptions, any intrinsic energy is a quasimetric. In goal-reaching control, optimal cost-to-go functions admit exactly this intrinsic form ; inversely, JEPAs trained to model intrinsic energies lie in the quasimetric value class targeted by QRL. Moreover, we observe why symmetric finite energies are structurally mismatched with one-way reachability, motivating asymmetric (quasimetric) energies when directionality matters.

### 🤖 AI 总结

**一句话总结**：文章从理论上证明：当 JEPA 的能量函数是由最小累计“努力”定义的内禀能量时，这个能量空间天然形成一个拟度量空间，与强化学习中的目标条件代价函数本质一致。

**研究动机**：现有 JEPA 多用对称的相似度/能量来学习表征，但在具有方向性的控制与到达任务中，代价往往是不对称的，因此需要澄清 JEPA 的能量形式与强化学习中“到目标代价”的数学关系。

**核心方法**：作者将 JEPA 的能量函数限制为“内禀（最小作用量）能量”，即在两状态间所有可行轨迹上对局部努力的累积取下确界，并在温和的闭包和可加性假设下证明其满足拟度量（quasimetric）性质，并将其与最优 cost-to-go 的形式进行对比。

**主要结论**：只要 JEPA 学习的是内禀能量，它们诱导的表示空间就是拟度量空间，恰好对应 QRL 中的最优 cost-to-go 类函数；同时，对称且有限的能量结构与单向可达性不匹配，因此在方向性任务中应采用不对称的拟度量能量建模。

**关键词**：深度学习, 神经网络, embedding, 检索, 表示学习, 能量模型, 目标导向控制, 强化学习, 价值函数预估, 不对称距离

**评分**：24

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12245v1) | [下载PDF](https://arxiv.org/pdf/2602.12245v1.pdf)

---

## [22. Olmix: A Framework for Data Mixing Throughout LM Development](https://arxiv.org/abs/2602.12237v1)

**作者**：Mayee F. Chen, Tyler Murray, David Heineman 等 8 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-02-12

### 📄 论文摘要

Data mixing -- determining the ratios of data from different domains -- is a first-order concern for training language models (LMs). While existing mixing methods show promise, they fall short when applied during real-world LM development. We present Olmix, a framework that addresses two such challenges. First, the configuration space for developing a mixing method is not well understood -- design choices across existing methods lack justification or consensus and overlook practical issues like data constraints. We conduct a comprehensive empirical study of this space, identifying which design choices lead to a strong mixing method. Second, in practice, the domain set evolves throughout LM development as datasets are added, removed, partitioned, and revised -- a problem setting largely unaddressed by existing works, which assume fixed domains. We study how to efficiently recompute the mixture after the domain set is updated, leveraging information from past mixtures. We introduce mixture reuse, a mechanism that reuses existing ratios and recomputes ratios only for domains affected by the update. Over a sequence of five domain-set updates mirroring real-world LM development, mixture reuse matches the performance of fully recomputing the mix after each update with 74% less compute and improves over training without mixing by 11.6% on downstream tasks.

### 🤖 AI 总结

**一句话总结**：Olmix 提出了一套贯穿大模型开发全周期的数据混配框架，在多轮数据集变更场景下高效更新各领域数据比例，同时保持性能。

**研究动机**：现有数据混配方法设计选择分散且缺乏系统性比较，而且大多假设领域集合固定，无法应对实际开发中数据不断增删和重划分的动态场景。

**核心方法**：作者系统实证分析不同混配设计空间（如约束、搜索策略等），并提出“mixture reuse”机制：在领域集合变更时复用旧混配比例，仅对受影响领域重新计算，从而节省计算。

**主要结论**：在模拟真实开发流程的五次领域集更新序列上，mixture reuse 在仅用 26% 计算量的情况下达到与每次完全重算相当的效果，并相对无混配训练在下游任务上带来约 11.6% 性能提升。

**关键词**：深度学习, 语言模型, 数据混合, 领域自适应, 训练数据配比, 模型开发流程, 增量更新, 混合比重复用, 大规模预训练, 下游任务性能提升, rag

**评分**：40

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12237v1) | [下载PDF](https://arxiv.org/pdf/2602.12237v1.pdf)

---

## [23. Categorical Flow Maps](https://arxiv.org/abs/2602.12233v1)

**作者**：Daan Roos, Oscar Davis, Floor Eijkelboom 等 8 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-12

### 📄 论文摘要

We introduce Categorical Flow Maps, a flow-matching method for accelerated few-step generation of categorical data via self-distillation. Building on recent variational formulations of flow matching and the broader trend towards accelerated inference in diffusion and flow-based models, we define a flow map towards the simplex that transports probability mass toward a predicted endpoint, yielding a parametrisation that naturally constrains model predictions. Since our trajectories are continuous rather than discrete, Categorical Flow Maps can be trained with existing distillation techniques, as well as a new objective based on endpoint consistency. This continuous formulation also automatically unlocks test-time inference: we can directly reuse existing guidance and reweighting techniques in the categorical setting to steer sampling toward downstream objectives. Empirically, we achieve state-of-the-art few-step results on images, molecular graphs, and text, with strong performance even in single-step generation.

### 🤖 AI 总结

**一句话总结**：提出一种针对离散/类别数据的流匹配新框架 Categorical Flow Maps，通过连续化到单纯形并结合自蒸馏，实现图像、分子图和文本的高质量少步甚至单步生成。

**研究动机**：现有扩散与流模型在类别数据上通常需要较多采样步数且离散结构限制了蒸馏与指导等加速技术的使用，因此需要一种既适合离散数据又能高效少步生成的统一方法。

**核心方法**：在单纯形上定义从初始分布到预测终点分布的连续流映射，使概率质量沿连续轨迹移动并天然满足概率约束；在此基础上结合现有蒸馏技术与新的“终点一致性”目标进行训练，并在推理阶段复用连续流匹配领域的指导与重加权技巧来引导类别采样。

**主要结论**：该方法在图像、分子图和文本等离散任务上实现了当前最优的少步生成效果，即使在单步生成场景也保持较强性能，同时证明连续化的类别流映射既能加速推理又能灵活支持各类下游目标引导。

**关键词**：扩散模型, flow matching, 自蒸馏, 生成模型, 分类数据建模, 端点一致性训练, 连续轨迹采样, 图像分子图文本生成, diffusion

**评分**：47

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12233v1) | [下载PDF](https://arxiv.org/pdf/2602.12233v1.pdf)

---

## [24. Diffusion Alignment Beyond KL: Variance Minimisation as Effective Policy Optimiser](https://arxiv.org/abs/2602.12229v1)

**作者**：Zijing Ou, Jacob Si, Junyi Zhu 等 7 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-12

### 📄 论文摘要

Diffusion alignment adapts pretrained diffusion models to sample from reward-tilted distributions along the denoising trajectory. This process naturally admits a Sequential Monte Carlo (SMC) interpretation, where the denoising model acts as a proposal and reward guidance induces importance weights. Motivated by this view, we introduce Variance Minimisation Policy Optimisation (VMPO), which formulates diffusion alignment as minimising the variance of log importance weights rather than directly optimising a Kullback-Leibler (KL) based objective. We prove that the variance objective is minimised by the reward-tilted target distribution and that, under on-policy sampling, its gradient coincides with that of standard KL-based alignment. This perspective offers a common lens for understanding diffusion alignment. Under different choices of potential functions and variance minimisation strategies, VMPO recovers various existing methods, while also suggesting new design directions beyond KL.

### 🤖 AI 总结

**一句话总结**：本文将扩散对齐视为一个带重要性采样的SMC过程，提出用“对数重要性权重方差最小化”替代传统KL作为更统一有效的扩散策略优化目标。

**研究动机**：现有扩散对齐方法多以KL为目标，难以统一理解不同算法形式，且在采样效率和稳定性上存在不足，因此作者尝试从重要性采样方差的角度重新刻画与优化对齐过程。

**核心方法**：作者将扩散对齐建模为SMC：去噪模型是proposal，奖励引入importance weight，并提出VMPO，将优化目标设为最小化log重要性权重的方差；理论上证明其最优解是奖励倾斜分布，且在on-policy条件下梯度与KL对齐等价，并展示不同势函数与方差最小化策略如何统一并扩展已有方法。

**主要结论**：VMPO提供了一个以方差最小化为核心的统一视角，将多种扩散对齐方法归一到同一框架中，并在不局限于KL的前提下给出新的设计维度，理论上保持与KL目标一致的最优分布，同时为构造更稳定、高效的扩散对齐算法提供了方向。

**关键词**：扩散模型, 生成式建模, policy优化, variance minimisation, 奖励建模, Sequential Monte Carlo, importance sampling, 对齐方法, 采样策略, 目标分布, diffusion

**评分**：35

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12229v1) | [下载PDF](https://arxiv.org/pdf/2602.12229v1.pdf)

---

## [25. Towards On-Policy SFT: Distribution Discriminant Theory and its Applications in LLM Training](https://arxiv.org/abs/2602.12222v1)

**作者**：Miaosen Zhang, Yishan Liu, Shuxia Lin 等 11 位作者  
**分类**：cs.LG, cs.AI, cs.CV  
**发布时间**：2026-02-12

### 📄 论文摘要

Supervised fine-tuning (SFT) is computationally efficient but often yields inferior generalization compared to reinforcement learning (RL). This gap is primarily driven by RL's use of on-policy data. We propose a framework to bridge this chasm by enabling On-Policy SFT. We first present \textbf{\textit{Distribution Discriminant Theory (DDT)}}, which explains and quantifies the alignment between data and the model-induced distribution. Leveraging DDT, we introduce two complementary techniques: (i) \textbf{\textit{In-Distribution Finetuning (IDFT)}}, a loss-level method to enhance generalization ability of SFT, and (ii) \textbf{\textit{Hinted Decoding}}, a data-level technique that can re-align the training corpus to the model's distribution. Extensive experiments demonstrate that our framework achieves generalization performance on par with prominent offline RL algorithms, including DPO and SimPO, while maintaining the efficiency of an SFT pipeline. The proposed framework thus offers a practical alternative in domains where RL is infeasible. We open-source the code here: https://github.com/zhangmiaosen2000/Towards-On-Policy-SFT

### 🤖 AI 总结

**一句话总结**：论文提出分布判别理论（DDT）及其衍生的在分布微调和提示解码方法，使传统SFT在保持高效的同时接近离线RL（如DPO、SimPO）的泛化性能。

**研究动机**：现有SFT虽然高效但因使用离线、脱策略数据，泛化明显弱于使用在线（on-policy）数据的RL方法，因此需要在不引入复杂RL训练的前提下，让SFT具备类似on-policy优势。

**核心方法**：作者提出分布判别理论（DDT）用于定量刻画训练数据与模型诱导分布的对齐程度，并基于此设计：1）在损失层面重新加权与调整的在分布微调（IDFT），2）通过特殊解码/提示策略重构训练语料分布的提示解码（Hinted Decoding），从而实现“On-Policy SFT”。

**主要结论**：实验表明，该On-Policy SFT框架在多个任务上的泛化性能可与DPO、SimPO等主流离线RL算法相当，同时保留SFT的计算与实现简洁性，为RL不易部署的场景提供了实用替代方案，并已开源实现。

**关键词**：大语言模型, 监督微调, On-Policy SFT, 分布判别理论, In-Distribution Finetuning, Hinted Decoding, 离线强化学习, DPO, SimPO, 对齐泛化能力

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12222v1) | [下载PDF](https://arxiv.org/pdf/2602.12222v1.pdf)

---

## [26. The Observer Effect in World Models: Invasive Adaptation Corrupts Latent Physics](https://arxiv.org/abs/2602.12218v1)

**作者**：Christian Internò, Jumpei Yamaguchi, Loren Amdahl-Culleton 等 6 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-12

### 📄 论文摘要

Determining whether neural models internalize physical laws as world models, rather than exploiting statistical shortcuts, remains challenging, especially under out-of-distribution (OOD) shifts. Standard evaluations often test latent capability via downstream adaptation (e.g., fine-tuning or high-capacity probes), but such interventions can change the representations being measured and thus confound what was learned during self-supervised learning (SSL). We propose a non-invasive evaluation protocol, PhyIP. We test whether physical quantities are linearly decodable from frozen representations, motivated by the linear representation hypothesis. Across fluid dynamics and orbital mechanics, we find that when SSL achieves low error, latent structure becomes linearly accessible. PhyIP recovers internal energy and Newtonian inverse-square scaling on OOD tests (e.g., $ρ> 0.90$). In contrast, adaptation-based evaluations can collapse this structure ($ρ\approx 0.05$). These findings suggest that adaptation-based evaluation can obscure latent structures and that low-capacity probes offer a more accurate evaluation of physical world models.

### 🤖 AI 总结

**一句话总结**：论文指出，用高容量下游适配来评估世界模型会“动摇”其潜在表征，从而掩盖模型已学到的物理结构，低容量线性探针更能如实反映潜在物理世界模型。

**研究动机**：现有评估常通过微调或高容量探针来检测神经网络是否学到物理规律，但这些适配本身会改变潜在表示，使人难以区分自监督阶段真正学到的物理结构与适配阶段新引入的“投机捷径”。

**核心方法**：作者提出非侵入评估协议 PhyIP，在流体力学和轨道力学任务上冻结自监督训练好的模型，仅用低容量线性探针解码潜在物理量（如内能、反平方定律参数），并对比与微调等适配式评估在分布外情形下的表现。

**主要结论**：当自监督误差较低时，物理量在潜在空间中变得线性可解码，PhyIP 可在 OOD 测试中恢复高相关的内能和牛顿反平方结构，而基于适配的评估反而会破坏这种结构，说明对物理世界模型的评估应优先使用低容量、非侵入式探针而非高容量适配。

**关键词**：神经网络, 自监督学习, 物理世界模型, 线性可分表示, 低容量probe, 流体力学模拟, 轨道力学预测, OOD泛化分析, agent

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12218v1) | [下载PDF](https://arxiv.org/pdf/2602.12218v1.pdf)

---

## [27. Learning to Forget Attention: Memory Consolidation for Adaptive Compute Reduction](https://arxiv.org/abs/2602.12204v1)

**作者**：Ibne Farabi Shihab, Sanjeda Akter, Anuj Sharma  
**分类**：cs.LG  
**发布时间**：2026-02-12

### 📄 论文摘要

Hybrid architectures combining state-space models with attention have achieved strong efficiency-quality tradeoffs, yet existing approaches either apply attention uniformly or learn static sparse patterns. This misses a key opportunity: \emph{attention demand should decrease over time as recurring patterns become familiar}. We present a surprising finding from analyzing GPT-2 models: \textbf{88\%} of attention operations retrieve information already predictable from the model's hidden state, and this redundancy does \emph{not} decrease during training. Motivated by this observation, we introduce \textbf{\ours{}} (\textbf{C}onsolidation-based \textbf{R}outing for \textbf{A}daptive \textbf{M}emory), a biologically inspired memory consolidation mechanism that gradually distills episodic retrievals into parametric semantic memory. Unlike prior sparse attention methods, \ours{} exhibits \emph{decreasing attention utilization} over training, achieving a \textbf{37.8$\times$} reduction through a sharp phase transition at approximately 3K steps. We prove that this capability is \emph{impossible} without consolidation: any static routing scheme requires $Ω(f \cdot n)$ attention for tasks with recurring patterns of frequency $f$. On our proposed SRCD benchmark, \ours{} achieves \textbf{100\% retrieval accuracy} at 1.6\% attention compute (vs.\ 68\% for baselines), and consolidated patterns transfer to unseen tasks with \textbf{48--52\%} attention reduction without retraining. Remarkably, the learned consolidation dynamics quantitatively match human episodic-to-semantic memory transition curves from cognitive psychology ($γ= 0.43$ vs.\ $γ_{\text{human}} \approx 0.4$--$0.5$). Code and benchmarks are available at [anonymized].

### 🤖 AI 总结

**一句话总结**：论文提出一种名为CRAM的“会遗忘注意力”的记忆巩固机制，让模型在训练中逐步减少对注意力检索的依赖，大幅节省注意力计算而保持甚至提升性能。

**研究动机**：作者发现GPT-2中约88%的注意力操作在检索本就可由隐藏状态预测的信息，且这种冗余在训练过程中并不会自然下降，因此希望设计一种机制，让模型在遇到重复模式时能逐渐“学会不看”注意力，从而自适应降低计算量。

**核心方法**：提出CRAM（Consolidation-based Routing for Adaptive Memory）：通过将反复通过注意力检索到的“情景记忆”逐步蒸馏进参数化的“语义记忆”，并学习一个随训练进程演化的路由策略，使得模型在熟悉模式上逐渐绕过注意力，仅在新颖或未巩固的信息上使用注意力。

**主要结论**：理论上证明若没有巩固机制，任何静态路由在含重复模式的任务上都需要Ω(f·n)级别的注意力；实验证明CRAM在SRCD基准上在仅1.6%的注意力计算下仍达100%检索准确率，并在约3K步出现注意力使用的相变（总体减少37.8倍），且其巩固动力学与人类从情景记忆到语义记忆的转变曲线高度一致，并能零样本迁移到新任务时继续节省约50%的注意力。

**关键词**：深度学习, 神经网络, transformer, 注意力机制, 记忆巩固, 自适应计算, 稀疏路由, 参数化语义记忆, 序列建模, 语言模型

**评分**：40

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12204v1) | [下载PDF](https://arxiv.org/pdf/2602.12204v1.pdf)

---

## [28. How Sampling Shapes LLM Alignment: From One-Shot Optima to Iterative Dynamics](https://arxiv.org/abs/2602.12180v1)

**作者**：Yurong Chen, Yu He, Michael I. Jordan 等 4 位作者  
**分类**：cs.LG, cs.GT  
**发布时间**：2026-02-12

### 📄 论文摘要

Standard methods for aligning large language models with human preferences learn from pairwise comparisons among sampled candidate responses and regularize toward a reference policy. Despite their effectiveness, the effects of sampling and reference choices are poorly understood theoretically. We investigate these effects through Identity Preference Optimization, a widely used preference alignment framework, and show that proper instance-dependent sampling can yield stronger ranking guarantees, while skewed on-policy sampling can induce excessive concentration under structured preferences. We then analyze iterative alignment dynamics in which the learned policy feeds back into future sampling and reference policies, reflecting a common practice of model-generated preference data. We prove that these dynamics can exhibit persistent oscillations or entropy collapse for certain parameter choices, and characterize regimes that guarantee stability. Our theoretical insights extend to Direct Preference Optimization, indicating the phenomena we captured are common to a broader class of preference-alignment methods. Experiments on real-world preference data validate our findings.

### 🤖 AI 总结

**一句话总结**：本文从理论上分析了采样策略和参考策略如何塑造偏好对齐训练中的LLM行为，并揭示其可能导致更强排序性能、过度集中特性以及迭代训练中的振荡或熵坍缩。

**研究动机**：当前主流偏好对齐方法（如IPO/DPO）大量依赖从模型采样的候选回答和参考策略，但采样方式和参考选取对最终对齐效果和稳定性的作用缺乏系统理论理解。

**核心方法**：在“Identity Preference Optimization”框架下，形式化分析不同实例相关采样和偏置的on-policy采样对排序保证和分布熵的影响，并建立迭代对齐动力学模型（训练策略反哺后续采样与参考），推导出可能出现振荡、熵坍缩及其稳定条件，并将理论扩展到DPO等方法。

**主要结论**：合理的、实例依赖的采样可以显著提升偏好排序质量，而过度偏向当前策略的采样在结构化偏好下会导致分布过度集中；在迭代生成偏好数据的对齐流程中，不恰当的参数会产生持续振荡或熵坍缩，而在特定参数与设定下可保证收敛与稳定，这些现象同样适用于更广泛的偏好对齐方法并得到真实数据实验的支持。

**关键词**：大型语言模型, 偏好对齐, DirectPreferenceOptimization, 采样策略, 参考策略, 迭代训练动态, 稳定性分析, 熵塌缩, 人类反馈学习, 理论分析实验验证, llm

**评分**：35

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12180v1) | [下载PDF](https://arxiv.org/pdf/2602.12180v1.pdf)

---

## [29. Amortized Molecular Optimization via Group Relative Policy Optimization](https://arxiv.org/abs/2602.12162v1)

**作者**：Muhammad bin Javaid, Hasham Hussain, Ashima Khanna 等 8 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-12

### 📄 论文摘要

Molecular design encompasses tasks ranging from de-novo design to structural alteration of given molecules or fragments. For the latter, state-of-the-art methods predominantly function as "Instance Optimizers'', expending significant compute restarting the search for every input structure. While model-based approaches theoretically offer amortized efficiency by learning a policy transferable to unseen structures, existing methods struggle to generalize. We identify a key failure mode: the high variance arising from the heterogeneous difficulty of distinct starting structures. To address this, we introduce GRXForm, adapting a pre-trained Graph Transformer model that optimizes molecules via sequential atom-and-bond additions. We employ Group Relative Policy Optimization (GRPO) for goal-directed fine-tuning to mitigate variance by normalizing rewards relative to the starting structure. Empirically, GRXForm generalizes to out-of-distribution molecular scaffolds without inference-time oracle calls or refinement, achieving scores in multi-objective optimization competitive with leading instance optimizers.

### 🤖 AI 总结

**一句话总结**：本文提出GRXForm与Group Relative Policy Optimization方法，实现对分子结构的摊销式优化，并在无需推理时调用打分器的前提下取得接近实例优化器的性能且具备更强泛化能力。

**研究动机**：现有分子结构优化方法多为对每个输入结构单独搜索的“实例优化器”，计算成本高且难以将搜索策略泛化到新分子结构，而基于模型的策略优化又因不同起始分子难度差异大而导致高方差、泛化能力不足。

**核心方法**：作者基于预训练Graph Transformer构建GRXForm，通过序列化的原子和键添加来优化分子，并提出Group Relative Policy Optimization（GRPO），按起始分子分组并使用相对奖励归一化，以降低策略梯度方差并实现面向目标的微调。

**主要结论**：实验证明GRXForm在多目标分子优化任务上能对分布外骨架实现有效泛化，在无需推理时调用目标打分器或额外精修的情况下，其性能与领先的实例优化器相竞争，从而展示了摊销式分子优化的效率与实用性。

**关键词**：深度学习, transformer, 强化学习, 策略优化, 分子生成, 图神经网络, 多目标优化, 离线训练, 结构优化

**评分**：38

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12162v1) | [下载PDF](https://arxiv.org/pdf/2602.12162v1.pdf)

---

## [30. SafeNeuron: Neuron-Level Safety Alignment for Large Language Models](https://arxiv.org/abs/2602.12158v1)

**作者**：Zhaoxin Wang, Jiaming Liang, Fengbin Zhu 等 8 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-12

### 📄 论文摘要

Large language models (LLMs) and multimodal LLMs are typically safety-aligned before release to prevent harmful content generation. However, recent studies show that safety behaviors are concentrated in a small subset of parameters, making alignment brittle and easily bypassed through neuron-level attacks. Moreover, most existing alignment methods operate at the behavioral level, offering limited control over the model's internal safety mechanisms. In this work, we propose SafeNeuron, a neuron-level safety alignment framework that improves robustness by redistributing safety representations across the network. SafeNeuron first identifies safety-related neurons, then freezes these neurons during preference optimization to prevent reliance on sparse safety pathways and force the model to construct redundant safety representations. Extensive experiments across models and modalities demonstrate that SafeNeuron significantly improves robustness against neuron pruning attacks, reduces the risk of open-source models being repurposed as red-team generators, and preserves general capabilities. Furthermore, our layer-wise analysis reveals that safety behaviors are governed by stable and shared internal representations. Overall, SafeNeuron provides an interpretable and robust perspective for model alignment.

### 🤖 AI 总结

**一句话总结**：SafeNeuron 通过在神经元层面分散安全表示、构建冗余安全通路，显著提升大模型的安全鲁棒性，同时保持通用能力。

**研究动机**：现有安全对齐集中在少量参数和行为层面，容易被神经元剪枝等攻击绕过，且难以直接控制模型内部的安全机制，因此需要更精细、更稳健的内部对齐方法。

**核心方法**：SafeNeuron 首先识别负责安全行为的神经元并在偏好优化阶段冻结这些神经元，迫使模型在其他神经元中重建并冗余化安全表示，从而在网络各层分布更均匀的安全表征。

**主要结论**：实验表明，SafeNeuron 能显著提升模型在神经元剪枝攻击下的安全鲁棒性，降低开源模型被当作红队生成器滥用的风险，且基本不损伤通用能力；层级分析进一步显示安全行为依托稳定且可共享的内部表示，为安全对齐提供了更可解释的视角。

**关键词**：大语言模型, 安全对齐, 神经网络, 多模态LLM, 偏好优化, 神经元剪枝攻击, 表示学习, 模型鲁棒性

**评分**：40

**论文链接**：[查看原文](https://arxiv.org/abs/2602.12158v1) | [下载PDF](https://arxiv.org/pdf/2602.12158v1.pdf)

---

