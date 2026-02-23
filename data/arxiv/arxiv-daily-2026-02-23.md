# arXiv AI 论文日报 | 2026-02-23

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.LG](#csLG) (13 篇)
- [cs.CL](#csCL) (7 篇)
- [cs.CV](#csCV) (9 篇)
- [cs.AI](#csAI) (1 篇)

---

## cs.AI

## [1. Diffusing to Coordinate: Efficient Online Multi-Agent Diffusion Policies](https://arxiv.org/abs/2602.18291v1)

**作者**：Zhuoran Li, Hai Zhong, Xun Wang 等 6 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-20

### 📄 论文摘要

Online Multi-Agent Reinforcement Learning (MARL) is a prominent framework for efficient agent coordination. Crucially, enhancing policy expressiveness is pivotal for achieving superior performance. Diffusion-based generative models are well-positioned to meet this demand, having demonstrated remarkable expressiveness and multimodal representation in image generation and offline settings. Yet, their potential in online MARL remains largely under-explored. A major obstacle is that the intractable likelihoods of diffusion models impede entropy-based exploration and coordination. To tackle this challenge, we propose among the first \underline{O}nline off-policy \underline{MA}RL framework using \underline{D}iffusion policies (\textbf{OMAD}) to orchestrate coordination. Our key innovation is a relaxed policy objective that maximizes scaled joint entropy, facilitating effective exploration without relying on tractable likelihood. Complementing this, within the centralized training with decentralized execution (CTDE) paradigm, we employ a joint distributional value function to optimize decentralized diffusion policies. It leverages tractable entropy-augmented targets to guide the simultaneous updates of diffusion policies, thereby ensuring stable coordination. Extensive evaluations on MPE and MAMuJoCo establish our method as the new state-of-the-art across $10$ diverse tasks, demonstrating a remarkable $2.5\times$ to $5\times$ improvement in sample efficiency.

### 🤖 AI 总结

**一句话总结**：本文提出OMAD框架，将扩散策略引入在线多智能体强化学习，通过放松的熵目标与分布式价值函数实现高效协同与显著提升样本效率。

**研究动机**：现有在线多智能体RL在策略表达能力和复杂协同任务的探索方面受限，而扩散模型虽具强表达力，却因似然难以计算难以直接用于需要熵正则的在线MARL。

**核心方法**：提出在线离策略多智能体扩散策略框架OMAD：1）设计基于“缩放联合熵”的放松策略目标，在无需可 tractable 似然的前提下实现探索与协调；2）在CTDE架构下引入联合分布式价值函数，通过可计算的熵增强目标联合优化多个去中心化扩散策略，保证稳定协同更新。

**主要结论**：在MPE与MAMuJoCo的10个任务上，OMAD取得新的SOTA表现，相比现有方法样本效率提升约2.5–5倍，验证了扩散策略在在线多智能体强化学习中的有效性与协同能力优势。

**关键词**：多智能体强化学习, 扩散模型, 生成式策略, 联合熵最大化, 集中训练分散执行, 分布式价值函数, MPE环境, MAMuJoCo协调控制, agent

**评分**：40

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18291v1) | [下载PDF](https://arxiv.org/pdf/2602.18291v1.pdf)

---

## cs.CL

## [2. VIRAASAT: Traversing Novel Paths for Indian Cultural Reasoning](https://arxiv.org/abs/2602.18429v1)

**作者**：Harshul Raj Surana, Arijit Maji, Aryan Vats 等 6 位作者  
**分类**：cs.CL, cs.IR  
**发布时间**：2026-02-20

### 📄 论文摘要

Large Language Models (LLMs) have made significant progress in reasoning tasks across various domains such as mathematics and coding. However, their performance deteriorates in tasks requiring rich socio-cultural knowledge and diverse local contexts, particularly those involving Indian Culture. Existing Cultural benchmarks are (i) Manually crafted, (ii) contain single-hop questions testing factual recall, and (iii) prohibitively costly to scale, leaving this deficiency largely unmeasured. To address this, we introduce VIRAASAT, a novel, semi-automated multi-hop approach for generating cultural specific multi-hop Question-Answering dataset for Indian culture. VIRAASAT leverages a Knowledge Graph comprising more than 700 expert-curated cultural artifacts, covering 13 key attributes of Indian culture (history, festivals, etc). VIRAASAT spans all 28 states and 8 Union Territories, yielding more than 3,200 multi-hop questions that necessitate chained cultural reasoning. We evaluate current State-of-the-Art (SOTA) LLMs on VIRAASAT and identify key limitations in reasoning wherein fine-tuning on Chain-of-Thought(CoT) traces fails to ground and synthesize low-probability facts. To bridge this gap, we propose a novel framework named Symbolic Chain-of-Manipulation (SCoM). Adapting the Chain-of-Manipulation paradigm, we train the model to simulate atomic Knowledge Graph manipulations internally. SCoM teaches the model to reliably traverse the topological structure of the graph. Experiments on Supervised Fine-Tuning (SFT) demonstrate that SCoM outperforms standard CoT baselines by up to 20%. We release the VIRAASAT dataset along with our findings, laying a strong foundation towards building Culturally Aware Reasoning Models.

### 🤖 AI 总结

**一句话总结**：论文提出印度文化多跳推理数据集 VIRAASAT，并通过符号化的 Chain-of-Manipulation 训练框架 SCoM，显著提升大模型在印度文化推理上的表现。

**研究动机**：现有大模型在需要丰富社会文化与本地背景知识（尤其是印度文化）的多跳推理任务上表现较差，而现有文化基准多为人工单跳问答，规模小且难扩展，无法系统衡量这一缺陷。

**核心方法**：构建包含700+专家标注文化实体和13类属性的知识图谱，覆盖印度全部28邦和8个联邦属地，半自动生成3200+多跳文化问答数据集 VIRAASAT；并提出 SCoM 框架，让模型在内部模拟对知识图谱的原子操作，从而学习图结构遍历和符号化多跳推理。

**主要结论**：在监督微调场景下，SCoM 相比标准 Chain-of-Thought 基线在 VIRAASAT 上可提升最高约20%的表现，表明通过符号化图操作显式建模多跳推理，有助于构建更具文化感知能力的语言模型；作者同时公开数据集与实验结果，以推动文化推理研究。

**关键词**：大语言模型, LLM, 文化推理, 知识图谱问答, 多跳推理, 印度文化数据集, Chain-of-Thought, Symbolic Chain-of-Manipulation, SFT微调, 拓扑结构遍历

**评分**：26

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18429v1) | [下载PDF](https://arxiv.org/pdf/2602.18429v1.pdf)

---

## [3. RVR: Retrieve-Verify-Retrieve for Comprehensive Question Answering](https://arxiv.org/abs/2602.18425v1)

**作者**：Deniz Qian, Hung-Ting Chen, Eunsol Choi  
**分类**：cs.CL, cs.IR  
**发布时间**：2026-02-20

### 📄 论文摘要

Comprehensively retrieving diverse documents is crucial to address queries that admit a wide range of valid answers. We introduce retrieve-verify-retrieve (RVR), a multi-round retrieval framework designed to maximize answer coverage. Initially, a retriever takes the original query and returns a candidate document set, followed by a verifier that identifies a high-quality subset. For subsequent rounds, the query is augmented with previously verified documents to uncover answers that are not yet covered in previous rounds. RVR is effective even with off-the-shelf retrievers, and fine-tuning retrievers for our inference procedure brings further gains. Our method outperforms baselines, including agentic search approaches, achieving at least 10% relative and 3% absolute gain in complete recall percentage on a multi-answer retrieval dataset (QAMPARI). We also see consistent gains on two out-of-domain datasets (QUEST and WebQuestionsSP) across different base retrievers. Our work presents a promising iterative approach for comprehensive answer recall leveraging a verifier and adapting retrievers to a new inference scenario.

### 🤖 AI 总结

**一句话总结**：本文提出多轮检索框架RVR，通过“检索-验证-再检索”的循环显著提升多答案问题的全面召回率。

**研究动机**：传统单轮检索难以覆盖多答案问题中分布广泛且多样的相关文档，导致答案覆盖不全，尤其是在需要“所有正确答案”的场景中表现不足。

**核心方法**：RVR先用基础检索器对原始问题检索得到候选文档，再由验证器筛选出高质量子集；随后将这些已验证文档拼接入扩展查询，进行多轮新的检索，以补全尚未覆盖的答案，同时还探索针对该迭代推理场景对检索器进行微调。

**主要结论**：在QAMPARI多答案检索数据集上，RVR相对基线在完整召回率上至少提升10%相对值、3%绝对值，并在QUEST与WebQuestionsSP等跨领域数据集和不同底层检索器上均取得一致提升，表明借助验证器驱动的迭代检索是提升综合答案召回的有效范式。

**关键词**：检索增强生成, 多轮检索, verifier验证模型, query重写, 语义检索, 向量检索, agentic检索, 问答系统

**评分**：39

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18425v1) | [下载PDF](https://arxiv.org/pdf/2602.18425v1.pdf)

---

## [4. SPQ: An Ensemble Technique for Large Language Model Compression](https://arxiv.org/abs/2602.18420v1)

**作者**：Jiamin Yao, Eren Gultepe  
**分类**：cs.CL  
**发布时间**：2026-02-20

### 📄 论文摘要

This study presents an ensemble technique, SPQ (SVD-Pruning-Quantization), for large language model (LLM) compression that combines variance-retained singular value decomposition (SVD), activation-based pruning, and post-training linear quantization. Each component targets a different source of inefficiency: i) pruning removes redundant neurons in MLP layers, ii) SVD reduces attention projections into compact low-rank factors, iii) and 8-bit quantization uniformly compresses all linear layers. At matched compression ratios, SPQ outperforms individual methods (SVD-only, pruning-only, or quantization-only) in perplexity, demonstrating the benefit of combining complementary techniques. Applied to LLaMA-2-7B, SPQ achieves up to 75% memory reduction while maintaining or improving perplexity (e.g., WikiText-2 5.47 to 4.91) and preserving accuracy on downstream benchmarks such as C4, TruthfulQA, and GSM8K. Compared to strong baselines like GPTQ and SparseGPT, SPQ offers competitive perplexity and accuracy while using less memory (6.86 GB vs. 7.16 GB for GPTQ). Moreover, SPQ improves inference throughput over GPTQ, achieving up to a 1.9x speedup, which further enhances its practicality for real-world deployment. The effectiveness of SPQ's robust compression through layer-aware and complementary compression techniques may provide practical deployment of LLMs in memory-constrained environments. Code is available at: https://github.com/JiaminYao/SPQ_LLM_Compression/

### 🤖 AI 总结

**一句话总结**：SPQ 提出一种将SVD、剪枝和量化组合的集成压缩方法，在大幅降低LLM显存占用的同时保持甚至提升困惑度和下游任务表现。

**研究动机**：大模型在显存、存储和推理延迟上成本极高，现有单一压缩技术（仅剪枝、仅低秩分解或仅量化）往往难以在高压缩率下同时兼顾精度与效率，因此需要一种互补、多粒度的组合压缩方案。

**核心方法**：SPQ 面向不同结构采用互补策略：对 MLP 层基于激活重要性进行神经元剪枝，对注意力投影矩阵进行保留方差约束的低秩 SVD 分解，并对所有线性层进行 8bit 线性后训练量化，以层感知方式在整体上控制压缩率与精度损失。

**主要结论**：在 LLaMA-2-7B 上，SPQ 在相同压缩率下优于单一方法，在最高约 75% 内存压缩下仍能降低 WikiText-2 困惑度并保持 C4、TruthfulQA、GSM8K 等下游任务准确率，相比 GPTQ / SparseGPT 既更省显存又最高可提升约 1.9× 推理吞吐，表明该集成压缩技术适合在受限硬件环境中部署LLM。

**关键词**：大语言模型, LLM压缩, 模型剪枝, 低秩分解, SVD, 8bit量化, 推理加速, 内存优化, 模型部署

**评分**：38

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18420v1) | [下载PDF](https://arxiv.org/pdf/2602.18420v1.pdf)

---

## [5. Vichara: Appellate Judgment Prediction and Explanation for the Indian Judicial System](https://arxiv.org/abs/2602.18346v1)

**作者**：Pavithra PM Nair, Preethu Rose Anish  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-02-20

### 📄 论文摘要

In jurisdictions like India, where courts face an extensive backlog of cases, artificial intelligence offers transformative potential for legal judgment prediction. A critical subset of this backlog comprises appellate cases, which are formal decisions issued by higher courts reviewing the rulings of lower courts. To this end, we present Vichara, a novel framework tailored to the Indian judicial system that predicts and explains appellate judgments. Vichara processes English-language appellate case proceeding documents and decomposes them into decision points. Decision points are discrete legal determinations that encapsulate the legal issue, deciding authority, outcome, reasoning, and temporal context. The structured representation isolates the core determinations and their context, enabling accurate predictions and interpretable explanations. Vichara's explanations follow a structured format inspired by the IRAC (Issue-Rule-Application-Conclusion) framework and adapted for Indian legal reasoning. This enhances interpretability, allowing legal professionals to assess the soundness of predictions efficiently. We evaluate Vichara on two datasets, PredEx and the expert-annotated subset of the Indian Legal Documents Corpus (ILDC_expert), using four large language models: GPT-4o mini, Llama-3.1-8B, Mistral-7B, and Qwen2.5-7B. Vichara surpasses existing judgment prediction benchmarks on both datasets, with GPT-4o mini achieving the highest performance (F1: 81.5 on PredEx, 80.3 on ILDC_expert), followed by Llama-3.1-8B. Human evaluation of the generated explanations across Clarity, Linking, and Usefulness metrics highlights GPT-4o mini's superior interpretability.

### 🤖 AI 总结

**一句话总结**：Vichara 是一个面向印度司法体系的上诉判决预测与解释框架，通过结构化拆解判决文书显著提升预测准确性和可解释性。

**研究动机**：印度法院存在大量案件积压，其中上诉案件占比突出，现有判决预测方法对复杂的上诉结构与法律推理建模不足且解释性不强，因此需要一个既准确又便于法官和律师审查的预测与解释系统。

**核心方法**：Vichara 将英文上诉案件文书自动拆解为一系列 decision points（包含法律争点、裁决主体、结果、理由与时间背景），并采用改造后的 IRAC 结构生成解释；在 PredEx 和 ILDC_expert 数据集上用 GPT-4o mini、Llama-3.1-8B、Mistral-7B 和 Qwen2.5-7B 等大模型进行训练与评估。

**主要结论**：Vichara 在 PredEx 和 ILDC_expert 上均优于现有判决预测基线，其中 GPT-4o mini 的 F1 分别达到 81.5 和 80.3，人类评估也显示其生成的解释在清晰度、论证链条和实用性方面表现最佳，验证了该结构化表示与解释框架的有效性。

**关键词**：机器学习, 深度学习, 大语言模型, 法律判决预测, IRAC推理框架, 司法文书分析, 上诉案件判决解释, 印度司法系统, artificial intelligence

**评分**：47

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18346v1) | [下载PDF](https://arxiv.org/pdf/2602.18346v1.pdf)

---

## [6. Predicting Contextual Informativeness for Vocabulary Learning using Deep Learning](https://arxiv.org/abs/2602.18326v1)

**作者**：Tao Wu, Adam Kapelner  
**分类**：cs.CL  
**发布时间**：2026-02-20

### 📄 论文摘要

We describe a modern deep learning system that automatically identifies informative contextual examples (\qu{contexts}) for first language vocabulary instruction for high school student. Our paper compares three modeling approaches: (i) an unsupervised similarity-based strategy using MPNet's uniformly contextualized embeddings, (ii) a supervised framework built on instruction-aware, fine-tuned Qwen3 embeddings with a nonlinear regression head and (iii) model (ii) plus handcrafted context features. We introduce a novel metric called the Retention Competency Curve to visualize trade-offs between the discarded proportion of good contexts and the \qu{good-to-bad} contexts ratio providing a compact, unified lens on model performance. Model (iii) delivers the most dramatic gains with performance of a good-to-bad ratio of 440 all while only throwing out 70\% of the good contexts. In summary, we demonstrate that a modern embedding model on neural network architecture, when guided by human supervision, results in a low-cost large supply of near-perfect contexts for teaching vocabulary for a variety of target words.

### 🤖 AI 总结

**一句话总结**：本文构建并比较多种基于深度学习的模型，用于自动筛选适合高中生词汇学习的高质量语境例句。

**研究动机**：人工手工挑选词汇教学例句成本高且难以规模化，因此需要自动方法从大量文本中筛选真正有助记忆和理解的“好语境”。

**核心方法**：比较三种方法：(1) 使用MPNet语义相似度的无监督筛选；(2) 基于带教学指令微调的Qwen3嵌入加非线性回归头的有监督模型；(3) 在(2)的基础上加入手工设计的语境特征，并提出Retention Competency Curve评估“丢失好例句比例”与“好/坏例句比”之间的权衡。

**主要结论**：加入手工特征的有监督模型效果最佳，在仅丢弃约70%的好语境的情况下，实现约440:1的好/坏例句比，说明结合现代嵌入模型与人类标注监督可以低成本批量生成近乎完美的词汇教学语境。

**关键词**：深度学习, 神经网络, 语义检索, 文本嵌入, 监督学习, 非线性回归模型, 词汇学习场景, 教育技术应用, ml

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18326v1) | [下载PDF](https://arxiv.org/pdf/2602.18326v1.pdf)

---

## [7. PsihoRo: Depression and Anxiety Romanian Text Corpus](https://arxiv.org/abs/2602.18324v1)

**作者**：Alexandra Ciobotaru, Ana-Maria Bucur, Liviu P. Dinu  
**分类**：cs.CL  
**发布时间**：2026-02-20

### 📄 论文摘要

Psychological corpora in NLP are collections of texts used to analyze human psychology, emotions, and mental health. These texts allow researchers to study psychological constructs, detect mental health issues and analyze emotional language. However, mental health data can be difficult to collect correctly from social media, due to suppositions made by the collectors. A more pragmatic strategy involves gathering data through open-ended questions and then assessing this information with self-report screening surveys. This method was employed successfully for English, a language with a lot of psychological NLP resources. However, this cannot be stated for Romanian, which currently has no open-source mental health corpus. To address this gap, we have created the first corpus for depression and anxiety in Romanian, by utilizing a form with 6 open-ended questions along with the standardized PHQ-9 and GAD-7 screening questionnaires. Consisting of the texts of 205 respondents and although it may seem small, PsihoRo is a first step towards understanding and analyzing texts regarding the mental health of the Romanian population. We employ statistical analysis, text analysis using Romanian LIWC, emotion detection and topic modeling to show what are the most important features of this newly introduced resource to the NLP community.

### 🤖 AI 总结

**一句话总结**：本文构建并初步分析了首个罗马尼亚语抑郁与焦虑文本语料库 PsihoRo，用于心理健康相关的NLP研究。

**研究动机**：现有心理健康文本资源主要集中在英语，而罗马尼亚语缺乏开放的心理健康语料库，且社交媒体数据存在标注和推断偏差，因此需要一个基于标准量表与开放问答构建的可靠心理语料。

**核心方法**：作者通过包含6个开放式问题的问卷结合PHQ-9和GAD-7自评量表，从205名受试者收集罗马尼亚语文本，并利用统计分析、罗马尼亚版LIWC、情绪识别与主题建模等方法对语料特征进行系统探索。

**主要结论**：PsihoRo虽规模有限，但作为首个罗马尼亚语抑郁与焦虑语料库，为研究罗马尼亚人群心理健康相关文本提供了基础资源，并通过多种分析展示了该语料在心理与情绪语言研究中的可用性与价值。

**关键词**：机器学习, 深度学习, 神经网络, 情感分析, 心理健康检测, 罗马尼亚语文本分类, 抑郁焦虑识别, 心理语言学特征分析, 情绪识别, 主题模型分析, rag

**评分**：16

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18324v1) | [下载PDF](https://arxiv.org/pdf/2602.18324v1.pdf)

---

## [8. Simplifying Outcomes of Language Model Component Analyses with ELIA](https://arxiv.org/abs/2602.18262v1)

**作者**：Aaron Louis Eidt, Nils Feldhus  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-02-20

### 📄 论文摘要

While mechanistic interpretability has developed powerful tools to analyze the internal workings of Large Language Models (LLMs), their complexity has created an accessibility gap, limiting their use to specialists. We address this challenge by designing, building, and evaluating ELIA (Explainable Language Interpretability Analysis), an interactive web application that simplifies the outcomes of various language model component analyses for a broader audience. The system integrates three key techniques -- Attribution Analysis, Function Vector Analysis, and Circuit Tracing -- and introduces a novel methodology: using a vision-language model to automatically generate natural language explanations (NLEs) for the complex visualizations produced by these methods. The effectiveness of this approach was empirically validated through a mixed-methods user study, which revealed a clear preference for interactive, explorable interfaces over simpler, static visualizations. A key finding was that the AI-powered explanations helped bridge the knowledge gap for non-experts; a statistical analysis showed no significant correlation between a user's prior LLM experience and their comprehension scores, suggesting that the system reduced barriers to comprehension across experience levels. We conclude that an AI system can indeed simplify complex model analyses, but its true power is unlocked when paired with thoughtful, user-centered design that prioritizes interactivity, specificity, and narrative guidance.

### 🤖 AI 总结

**一句话总结**：本文提出并实现交互式可视化系统 ELIA，结合多种可解释性技术与自动自然语言讲解，帮助非专家理解大语言模型内部机理。

**研究动机**：当前机制可解释性工具复杂度高、使用门槛大，使大语言模型内部分析结果难以被非专业用户理解与使用。

**核心方法**：构建 ELIA Web 系统，将归因分析、功能向量分析和电路追踪三类方法集成在交互式界面中，并首次利用视觉-语言模型为复杂可视化自动生成自然语言解释，再通过混合方法用户研究评估效果。

**主要结论**：结果表明交互式、可探索界面优于静态可视化，AI 生成的解释显著缩小了不同经验用户间的理解差距，说明在以用户为中心的设计下，AI 系统可以有效简化复杂模型分析并提升可解释性可达性。

**关键词**：大语言模型, 解释性分析, 可视化解释, 自然语言生成, 交互式界面, 用户研究, 模型可解释性, llm

**评分**：40

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18262v1) | [下载PDF](https://arxiv.org/pdf/2602.18262v1.pdf)

---

## cs.CV

## [9. CapNav: Benchmarking Vision Language Models on Capability-conditioned Indoor Navigation](https://arxiv.org/abs/2602.18424v1)

**作者**：Xia Su, Ruiqi Chen, Benlin Liu 等 7 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-02-20

### 📄 论文摘要

Vision-Language Models (VLMs) have shown remarkable progress in Vision-Language Navigation (VLN), offering new possibilities for navigation decision-making that could benefit both robotic platforms and human users. However, real-world navigation is inherently conditioned by the agent's mobility constraints. For example, a sweeping robot cannot traverse stairs, while a quadruped can. We introduce Capability-Conditioned Navigation (CapNav), a benchmark designed to evaluate how well VLMs can navigate complex indoor spaces given an agent's specific physical and operational capabilities. CapNav defines five representative human and robot agents, each described with physical dimensions, mobility capabilities, and environmental interaction abilities. CapNav provides 45 real-world indoor scenes, 473 navigation tasks, and 2365 QA pairs to test if VLMs can traverse indoor environments based on agent capabilities. We evaluate 13 modern VLMs and find that current VLM's navigation performance drops sharply as mobility constraints tighten, and that even state-of-the-art models struggle with obstacle types that require reasoning on spatial dimensions. We conclude by discussing the implications for capability-aware navigation and the opportunities for advancing embodied spatial reasoning in future VLMs. The benchmark is available at https://github.com/makeabilitylab/CapNav

### 🤖 AI 总结

**一句话总结**：CapNav 提出一个面向“具身能力约束”的室内导航基准，用于系统评测视觉语言模型在不同机器人/人类能力条件下的导航与空间推理能力。

**研究动机**：现有视觉语言导航研究大多假设导航主体无明显行动约束，而现实中的机器人/人类具有尺寸、机动方式和交互能力等多种物理限制，需要评估模型在这些真实能力约束下的导航决策与空间理解。

**核心方法**：作者构建 CapNav 基准：定义5类典型人/机器人代理（含尺寸、机动与交互能力），基于45个真实室内场景设计473个导航任务和2365个问答样例，并在此上系统评测13个主流VLM在不同能力条件和障碍类型下的表现。

**主要结论**：实验发现随着机动约束变强，现有VLM导航性能急剧下降，尤其在需要精确空间尺寸与障碍类型推理的场景中表现不佳，说明当前模型的具身感知与能力感知导航仍很薄弱，未来需重点提升面向具体代理能力的空间推理与决策能力。

**关键词**：视觉语言模型, 多模态导航, 智能体, 室内路径规划, 具身智能, 能力约束场景, 机器人导航基准, 空间推理, agent

**评分**：36

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18424v1) | [下载PDF](https://arxiv.org/pdf/2602.18424v1.pdf)

---

## [10. Generated Reality: Human-centric World Simulation using Interactive Video Generation with Hand and Camera Control](https://arxiv.org/abs/2602.18422v1)

**作者**：Linxi Xie, Lisong C. Sun, Ashley Neall 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-20

### 📄 论文摘要

Extended reality (XR) demands generative models that respond to users' tracked real-world motion, yet current video world models accept only coarse control signals such as text or keyboard input, limiting their utility for embodied interaction. We introduce a human-centric video world model that is conditioned on both tracked head pose and joint-level hand poses. For this purpose, we evaluate existing diffusion transformer conditioning strategies and propose an effective mechanism for 3D head and hand control, enabling dexterous hand--object interactions. We train a bidirectional video diffusion model teacher using this strategy and distill it into a causal, interactive system that generates egocentric virtual environments. We evaluate this generated reality system with human subjects and demonstrate improved task performance as well as a significantly higher level of perceived amount of control over the performed actions compared with relevant baselines.

### 🤖 AI 总结

**一句话总结**：该工作提出一种面向XR的人体中心视频世界模型，可根据用户头部和手部姿态实时生成具身交互的第一人称虚拟环境。

**研究动机**：现有视频生成/世界模型主要依赖文本或按键等粗粒度控制，无法利用XR设备可获取的精细头部与手部运动数据，限制了沉浸式、具身交互体验。

**核心方法**：作者设计适用于3D头部和关节级手势的条件机制，系统性评估多种扩散Transformer条件策略，并以此训练双向视频扩散教师模型，再蒸馏为可因果推断、可交互的实时第一人称视频生成系统。

**主要结论**：用户实验显示，该“生成现实”系统相较相关基线显著提升任务完成表现，并让用户主观感受到更强的动作控制感，证明了基于头手姿态条件的交互式视频世界模型在XR中的实用价值。

**关键词**：生成式视频, 扩散模型, Diffusion Transformer, 三维手势控制, 头部姿态跟踪, 第一人称虚拟环境, XR交互, 人机交互实验

**评分**：41

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18422v1) | [下载PDF](https://arxiv.org/pdf/2602.18422v1.pdf)

---

## [11. Latent Equivariant Operators for Robust Object Recognition: Promise and Challenges](https://arxiv.org/abs/2602.18406v1)

**作者**：Minh Dinh, Stéphane Deny  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-02-20

### 📄 论文摘要

Despite the successes of deep learning in computer vision, difficulties persist in recognizing objects that have undergone group-symmetric transformations rarely seen during training-for example objects seen in unusual poses, scales, positions, or combinations thereof. Equivariant neural networks are a solution to the problem of generalizing across symmetric transformations, but require knowledge of transformations a priori. An alternative family of architectures proposes to earn equivariant operators in a latent space from examples of symmetric transformations. Here, using simple datasets of rotated and translated noisy MNIST, we illustrate how such architectures can successfully be harnessed for out-of-distribution classification, thus overcoming the limitations of both traditional and equivariant networks. While conceptually enticing, we discuss challenges ahead on the path of scaling these architectures to more complex datasets.

### 🤖 AI 总结

**一句话总结**：本文探讨在潜在空间中学习等变算子，以在无需显式先验群知识的情况下实现对旋转/平移等对称变换的稳健泛化。

**研究动机**：传统卷积网络难以泛化到训练中少见的姿态、尺度、位置组合，而群等变网络又依赖事先知道精确的对称群，限制了在复杂视觉任务中的应用，因此需要一种既能自动学习等变性又具OOD鲁棒性的架构。

**核心方法**：利用带噪声的旋转和平移MNIST构建对称变换样本，在潜在空间中学习等变算子，使潜在表示随输入图像的群变换按规则变化，并将该表示用于分类，以比较传统网络、显式等变网络与潜在等变方法在OOD场景下的表现。

**主要结论**：实验表明潜在等变算子可以在未见过的旋转/平移组合上显著提升分类性能，缓解传统与显式等变网络的局限，但作者指出在扩展到更复杂数据集和更高维度群结构时仍面临建模难度、数据需求和可扩展性等挑战。

**关键词**：深度学习, 神经网络, 等变神经网络, 潜在表示, 鲁棒目标识别, 姿态不变性, 旋转平移不变性, OOD泛化, MNIST数据集, 计算机视觉, deep learning

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18406v1) | [下载PDF](https://arxiv.org/pdf/2602.18406v1.pdf)

---

## [12. Self-Aware Object Detection via Degradation Manifolds](https://arxiv.org/abs/2602.18394v1)

**作者**：Stefan Becker, Simon Weiss, Wolfgang Hübner 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-20

### 📄 论文摘要

Object detectors achieve strong performance under nominal imaging conditions but can fail silently when exposed to blur, noise, compression, adverse weather, or resolution changes. In safety-critical settings, it is therefore insufficient to produce predictions without assessing whether the input remains within the detector's nominal operating regime. We refer to this capability as self-aware object detection.   We introduce a degradation-aware self-awareness framework based on degradation manifolds, which explicitly structure a detector's feature space according to image degradation rather than semantic content. Our method augments a standard detection backbone with a lightweight embedding head trained via multi-layer contrastive learning. Images sharing the same degradation composition are pulled together, while differing degradation configurations are pushed apart, yielding a geometrically organized representation that captures degradation type and severity without requiring degradation labels or explicit density modeling.   To anchor the learned geometry, we estimate a pristine prototype from clean training embeddings, defining a nominal operating point in representation space. Self-awareness emerges as geometric deviation from this reference, providing an intrinsic, image-level signal of degradation-induced shift that is independent of detection confidence.   Extensive experiments on synthetic corruption benchmarks, cross-dataset zero-shot transfer, and natural weather-induced distribution shifts demonstrate strong pristine-degraded separability, consistent behavior across multiple detector architectures, and robust generalization under semantic shift. These results suggest that degradation-aware representation geometry provides a practical and detector-agnostic foundation.

### 🤖 AI 总结

**一句话总结**：论文提出一种基于“退化流形”的自感知目标检测框架，使检测器能在图像质量退化时自识别出已超出其正常工作范围。

**研究动机**：现有目标检测器在模糊、噪声、压缩、恶劣天气和分辨率变化等退化条件下可能无声失败，仅靠检测置信度无法可靠判断输入是否仍在训练分布内，安全关键场景因此存在风险。

**核心方法**：在常规检测骨干网络上增加一个轻量嵌入头，通过多层对比学习使特征空间按“退化类型与强度”而非语义进行几何组织：相同退化配置的图像被拉近、不同配置被推远，并通过干净训练样本的嵌入估计“完好原型”作为名义工作点，利用与该原型的几何偏移度量自感知程度。

**主要结论**：实验表明该方法在多种合成退化、跨数据集零样本迁移及真实天气分布偏移下都能实现干净与退化图像的良好可分性，跨检测架构表现一致且对语义分布变化具有鲁棒泛化性，说明基于退化感知几何表示是一种实用且与检测器无关的自感知基础。

**关键词**：深度学习, 神经网络, 嵌入表示, 对比学习, 目标检测, 图像退化, 鲁棒性评估, 分布外检测, 自监督学习, 安全关键场景, embedding

**评分**：39

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18394v1) | [下载PDF](https://arxiv.org/pdf/2602.18394v1.pdf)

---

## [13. G-LoG Bi-filtration for Medical Image Classification](https://arxiv.org/abs/2602.18329v1)

**作者**：Qingsong Wang, Jiaxing He, Bingzhe Hou 等 6 位作者  
**分类**：cs.CV, math.AT  
**发布时间**：2026-02-20

### 📄 论文摘要

Building practical filtrations on objects to detect topological and geometric features is an important task in the field of Topological Data Analysis (TDA). In this paper, leveraging the ability of the Laplacian of Gaussian operator to enhance the boundaries of medical images, we define the G-LoG (Gaussian-Laplacian of Gaussian) bi-filtration to generate the features more suitable for multi-parameter persistence module. By modeling volumetric images as bounded functions, then we prove the interleaving distance on the persistence modules obtained from our bi-filtrations on the bounded functions is stable with respect to the maximum norm of the bounded functions. Finally, we conduct experiments on the MedMNIST dataset, comparing our bi-filtration against single-parameter filtration and the established deep learning baselines, including Google AutoML Vision, ResNet, AutoKeras and auto-sklearn. Experiments results demonstrate that our bi-filtration significantly outperforms single-parameter filtration. Notably, a simple Multi-Layer Perceptron (MLP) trained on the topological features generated by our bi-filtration achieves performance comparable to complex deep learning models trained on the original dataset.

### 🤖 AI 总结

**一句话总结**：论文提出一种基于高斯-拉普拉斯算子的G-LoG双参数过滤方法，用拓扑特征实现医学图像分类，在MedMNIST上接近甚至媲美复杂深度学习模型。

**研究动机**：单参数TDA过滤在捕捉医学图像中复杂的拓扑与几何结构方面存在局限，且需要更稳定、可用于多参数持久同调的特征来提升医学影像分类表现。

**核心方法**：将三维医学图像建模为有界函数，引入结合高斯与LoG的G-LoG双参数过滤构造多参数持久模，并证明其在最大范数意义下的稳定性，然后用MLP对生成的拓扑特征进行分类并与主流深度学习和AutoML方法比较。

**主要结论**：G-LoG双参数过滤相较单参数过滤在MedMNIST上显著提升分类性能，且简单MLP基于其拓扑特征即可达到与复杂深度学习模型相当的效果，表明该TDA方法在医学图像分析中具有实际可用性和竞争力。

**关键词**：深度学习, 神经网络, 多层感知机MLP, 医学图像分类, 拓扑数据分析TDA, 多参数持久同调, 特征提取, MedMNIST数据集

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18329v1) | [下载PDF](https://arxiv.org/pdf/2602.18329v1.pdf)

---

## [14. Unifying Color and Lightness Correction with View-Adaptive Curve Adjustment for Robust 3D Novel View Synthesis](https://arxiv.org/abs/2602.18322v1)

**作者**：Ziteng Cui, Shuhong Liu, Xiaoyu Dong 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-20

### 📄 论文摘要

High-quality image acquisition in real-world environments remains challenging due to complex illumination variations and inherent limitations of camera imaging pipelines. These issues are exacerbated in multi-view capture, where differences in lighting, sensor responses, and image signal processor (ISP) configurations introduce photometric and chromatic inconsistencies that violate the assumptions of photometric consistency underlying modern 3D novel view synthesis (NVS) methods, including Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS), leading to degraded reconstruction and rendering quality. We propose Luminance-GS++, a 3DGS-based framework for robust NVS under diverse illumination conditions. Our method combines a globally view-adaptive lightness adjustment with a local pixel-wise residual refinement for precise color correction. We further design unsupervised objectives that jointly enforce lightness correction and multi-view geometric and photometric consistency. Extensive experiments demonstrate state-of-the-art performance across challenging scenarios, including low-light, overexposure, and complex luminance and chromatic variations. Unlike prior approaches that modify the underlying representation, our method preserves the explicit 3DGS formulation, improving reconstruction fidelity while maintaining real-time rendering efficiency.

### 🤖 AI 总结

**一句话总结**：Luminance-GS++在保持3D高斯渲染框架不变的前提下，通过视角自适应亮度曲线和局部颜色残差校正，实现在复杂光照条件下更鲁棒的三维新视角合成。

**研究动机**：现实多视角采集中由于光照变化、相机传感器差异和ISP配置不一致，导致图像间光度和色彩不一致，破坏NeRF/3DGS依赖的光度一致性假设，从而降低重建和渲染质量。

**核心方法**：基于3D Gaussian Splatting框架，提出全局视角自适应的亮度调整曲线结合逐像素残差颜色精修，并通过无监督损失联合约束亮度校正、多视角几何一致性和光度一致性。

**主要结论**：在低照度、过曝及复杂亮度/色彩变化场景上，该方法在保持3DGS显式表示和实时渲染效率的同时，显著提升了重建和新视角渲染质量，达到或超过现有方法的最新水平。

**关键词**：深度学习, 神经网络, NeRF新视图合成, 3DGaussianSplatting, 三维重建渲染, 光照自适应校正, 颜色恒常性, 多视图一致性约束, 实时渲染框架, agent

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18322v1) | [下载PDF](https://arxiv.org/pdf/2602.18322v1.pdf)

---

## [15. Diff2DGS: Reliable Reconstruction of Occluded Surgical Scenes via 2D Gaussian Splatting](https://arxiv.org/abs/2602.18314v1)

**作者**：Tianyi Song, Danail Stoyanov, Evangelos Mazomenos 等 4 位作者  
**分类**：cs.CV, cs.GR, cs.RO  
**发布时间**：2026-02-20

### 📄 论文摘要

Real-time reconstruction of deformable surgical scenes is vital for advancing robotic surgery, improving surgeon guidance, and enabling automation. Recent methods achieve dense reconstructions from da Vinci robotic surgery videos, with Gaussian Splatting (GS) offering real-time performance via graphics acceleration. However, reconstruction quality in occluded regions remains limited, and depth accuracy has not been fully assessed, as benchmarks like EndoNeRF and StereoMIS lack 3D ground truth. We propose Diff2DGS, a novel two-stage framework for reliable 3D reconstruction of occluded surgical scenes. In the first stage, a diffusion-based video module with temporal priors inpaints tissue occluded by instruments with high spatial-temporal consistency. In the second stage, we adapt 2D Gaussian Splatting (2DGS) with a Learnable Deformation Model (LDM) to capture dynamic tissue deformation and anatomical geometry. We also extend evaluation beyond prior image-quality metrics by performing quantitative depth accuracy analysis on the SCARED dataset. Diff2DGS outperforms state-of-the-art approaches in both appearance and geometry, reaching 38.02 dB PSNR on EndoNeRF and 34.40 dB on StereoMIS. Furthermore, our experiments demonstrate that optimizing for image quality alone does not necessarily translate into optimal 3D reconstruction accuracy. To address this, we further optimize the depth quality of the reconstructed 3D results, ensuring more faithful geometry in addition to high-fidelity appearance.

### 🤖 AI 总结

**一句话总结**：Diff2DGS通过“扩散视频补全 + 可形变2D Gaussian Splatting”两阶段框架，实现对被器械遮挡的手术场景进行更精确、更稳定的实时3D重建。

**研究动机**：现有基于手术内窥镜视频的3D重建在遮挡区域重建质量差且缺乏带真实3D几何真值的数据集，导致形变组织的深度和几何精度难以可靠评估与提升。

**核心方法**：首先使用引入时间先验的扩散式视频修补模块，对被手术器械遮挡的组织区域进行时空一致的补全；随后结合可学习形变模型的2D Gaussian Splatting，对动态组织形变和解剖几何进行建模与渲染，并在SCARED数据集上加入深度精度优化与评估。

**主要结论**：Diff2DGS在EndoNeRF与StereoMIS上显著提升PSNR并在外观和几何上优于现有方法，且实验表明仅优化图像质量无法保证3D几何精度，因此引入深度质量优化可获得更加可靠、逼真的手术场景3D重建。

**关键词**：扩散模型, 深度学习, 生成式, 神经网络, 视频修复, 2DGaussianSplatting, 可变形场景重建, 机器人手术导航, 内窥镜三维重建, 深度估计与评估, diffusion

**评分**：43

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18314v1) | [下载PDF](https://arxiv.org/pdf/2602.18314v1.pdf)

---

## [16. Multi-Level Conditioning by Pairing Localized Text and Sketch for Fashion Image Generation](https://arxiv.org/abs/2602.18309v1)

**作者**：Ziyue Liu, Davide Talon, Federico Girella 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-20

### 📄 论文摘要

Sketches offer designers a concise yet expressive medium for early-stage fashion ideation by specifying structure, silhouette, and spatial relationships, while textual descriptions complement sketches to convey material, color, and stylistic details. Effectively combining textual and visual modalities requires adherence to the sketch visual structure when leveraging the guidance of localized attributes from text. We present LOcalized Text and Sketch with multi-level guidance (LOTS), a framework that enhances fashion image generation by combining global sketch guidance with multiple localized sketch-text pairs. LOTS employs a Multi-level Conditioning Stage to independently encode local features within a shared latent space while maintaining global structural coordination. Then, the Diffusion Pair Guidance stage integrates both local and global conditioning via attention-based guidance within the diffusion model's multi-step denoising process. To validate our method, we develop Sketchy, the first fashion dataset where multiple text-sketch pairs are provided per image. Sketchy provides high-quality, clean sketches with a professional look and consistent structure. To assess robustness beyond this setting, we also include an "in the wild" split with non-expert sketches, featuring higher variability and imperfections. Experiments demonstrate that our method strengthens global structural adherence while leveraging richer localized semantic guidance, achieving improvement over state-of-the-art. The dataset, platform, and code are publicly available.

### 🤖 AI 总结

**一句话总结**：该论文提出LOTS框架，通过多层次结合全局草图和局部文本-草图对，实现更精确的服装图像生成。

**研究动机**：现有时尚图像生成方法难以同时严格遵守草图结构并细致反映局部文本描述（如材质、颜色、细节），尤其在非专业草图场景下鲁棒性不足。

**核心方法**：LOTS首先在多级条件编码阶段，将全局草图和多个局部文本-草图对编码到共享潜空间，既保持整体结构又捕捉局部特征；随后在扩散生成中通过注意力引导的“Diffusion Pair Guidance”，在每一步去噪中融合全局与局部条件约束。

**主要结论**：在作者构建的Sketchy多文本-草图对时尚数据集（含专业与“野外”非专业草图）上，LOTS显著提升了对全局结构的遵从与局部语义细节的表达效果，优于现有最新方法，相关数据集与代码已开源。

**关键词**：深度学习, 扩散模型, 多模态生成, 条件图像生成, 时尚图像生成, 草图到图像, 文本引导生成, 注意力机制, 潜在空间编码, 局部特征对齐, diffusion

**评分**：38

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18309v1) | [下载PDF](https://arxiv.org/pdf/2602.18309v1.pdf)

---

## [17. DEIG: Detail-Enhanced Instance Generation with Fine-Grained Semantic Control](https://arxiv.org/abs/2602.18282v1)

**作者**：Shiyan Du, Conghan Yue, Xinyu Cheng 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-20

### 📄 论文摘要

Multi-Instance Generation has advanced significantly in spatial placement and attribute binding. However, existing approaches still face challenges in fine-grained semantic understanding, particularly when dealing with complex textual descriptions. To overcome these limitations, we propose DEIG, a novel framework for fine-grained and controllable multi-instance generation. DEIG integrates an Instance Detail Extractor (IDE) that transforms text encoder embeddings into compact, instance-aware representations, and a Detail Fusion Module (DFM) that applies instance-based masked attention to prevent attribute leakage across instances. These components enable DEIG to generate visually coherent multi-instance scenes that precisely match rich, localized textual descriptions. To support fine-grained supervision, we construct a high-quality dataset with detailed, compositional instance captions generated by VLMs. We also introduce DEIG-Bench, a new benchmark with region-level annotations and multi-attribute prompts for both humans and objects. Experiments demonstrate that DEIG consistently outperforms existing approaches across multiple benchmarks in spatial consistency, semantic accuracy, and compositional generalization. Moreover, DEIG functions as a plug-and-play module, making it easily integrable into standard diffusion-based pipelines.

### 🤖 AI 总结

**一句话总结**：DEIG提出一种细粒度、可控的多实例生成框架，通过更精确的实例语义建模与注意力控制，实现与复杂文本描述高度匹配的图像生成。

**研究动机**：现有多实例生成方法在面对复杂、细粒度文本描述时，容易出现语义理解不足和跨实例属性混淆，难以保证空间一致性与属性精确绑定。

**核心方法**：DEIG设计了实例细节提取器IDE，将文本编码器的嵌入压缩为实例级语义表示，并通过细节融合模块DFM的实例掩码注意力抑制属性泄漏；同时构建高质量细粒度实例描述数据集和带区域标注、多属性提示的DEIG-Bench用于监督与评测。

**主要结论**：实验表明，DEIG在空间一致性、语义准确性和组合泛化方面显著优于现有方法，且作为即插即用模块可无缝集成到标准扩散模型流水线中。

**关键词**：深度学习, 神经网络, 生成式模型, 多实例图像生成, 细粒度语义控制, 文本嵌入表示, 掩码注意力机制, 扩散模型, 可组合图像合成, 基准数据集构建, diffusion

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18282v1) | [下载PDF](https://arxiv.org/pdf/2602.18282v1.pdf)

---

## cs.LG

## [18. Assigning Confidence: K-partition Ensembles](https://arxiv.org/abs/2602.18435v1)

**作者**：Aggelos Semoglou, John Pavlopoulos  
**分类**：cs.LG  
**发布时间**：2026-02-20

### 📄 论文摘要

Clustering is widely used for unsupervised structure discovery, yet it offers limited insight into how reliable each individual assignment is. Diagnostics, such as convergence behavior or objective values, may reflect global quality, but they do not indicate whether particular instances are assigned confidently, especially for initialization-sensitive algorithms like k-means. This assignment-level instability can undermine both accuracy and robustness. Ensemble approaches improve global consistency by aggregating multiple runs, but they typically lack tools for quantifying pointwise confidence in a way that combines cross-run agreement with geometric support from the learned cluster structure. We introduce CAKE (Confidence in Assignments via K-partition Ensembles), a framework that evaluates each point using two complementary statistics computed over a clustering ensemble: assignment stability and consistency of local geometric fit. These are combined into a single, interpretable score in [0,1]. Our theoretical analysis shows that CAKE remains effective under noise and separates stable from unstable points. Experiments on synthetic and real-world datasets indicate that CAKE effectively highlights ambiguous points and stable core members, providing a confidence ranking that can guide filtering or prioritization to improve clustering quality.

### 🤖 AI 总结

**一句话总结**：论文提出CAKE框架，通过聚类集成评估每个样本的聚类置信度，给出0到1之间的可解释打分。

**研究动机**：传统聚类只能给出整体结果，无法衡量单个点被分配到某簇是否可靠，尤其在对初始化敏感的算法（如k-means）中，点级不稳定会影响准确性和鲁棒性。

**核心方法**：构造多次聚类的k-partition集成，从中计算每个点的两类统计量：跨运行的一致性（assignment stability）和在各簇局部几何结构中的拟合一致性，并将二者融合为一个置信度得分。

**主要结论**：理论分析表明CAKE在噪声下仍能区分稳定与不稳定点；实验结果显示其能有效标出模糊边界点和稳定核心点，为过滤或优先处理样本以提升聚类质量提供了有用的置信排序。

**关键词**：机器学习, 聚类不确定性评估, 无监督结构发现, 聚类集成方法, 点级置信度评分, 局部几何一致性, 聚类结果稳定性, 噪声鲁棒性分析, 数据点优先级筛选, agent

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18435v1) | [下载PDF](https://arxiv.org/pdf/2602.18435v1.pdf)

---

## [19. The Geometry of Noise: Why Diffusion Models Don't Need Noise Conditioning](https://arxiv.org/abs/2602.18428v1)

**作者**：Mojtaba Sahraee-Ardakan, Mauricio Delbracio, Peyman Milanfar  
**分类**：cs.LG, cs.CV, eess.IV  
**发布时间**：2026-02-20

### 📄 论文摘要

Autonomous (noise-agnostic) generative models, such as Equilibrium Matching and blind diffusion, challenge the standard paradigm by learning a single, time-invariant vector field that operates without explicit noise-level conditioning. While recent work suggests that high-dimensional concentration allows these models to implicitly estimate noise levels from corrupted observations, a fundamental paradox remains: what is the underlying landscape being optimized when the noise level is treated as a random variable, and how can a bounded, noise-agnostic network remain stable near the data manifold where gradients typically diverge? We resolve this paradox by formalizing Marginal Energy, $E_{\text{marg}}(\mathbf{u}) = -\log p(\mathbf{u})$, where $p(\mathbf{u}) = \int p(\mathbf{u}|t)p(t)dt$ is the marginal density of the noisy data integrated over a prior distribution of unknown noise levels. We prove that generation using autonomous models is not merely blind denoising, but a specific form of Riemannian gradient flow on this Marginal Energy. Through a novel relative energy decomposition, we demonstrate that while the raw Marginal Energy landscape possesses a $1/t^p$ singularity normal to the data manifold, the learned time-invariant field implicitly incorporates a local conformal metric that perfectly counteracts the geometric singularity, converting an infinitely deep potential well into a stable attractor. We also establish the structural stability conditions for sampling with autonomous models. We identify a ``Jensen Gap'' in noise-prediction parameterizations that acts as a high-gain amplifier for estimation errors, explaining the catastrophic failure observed in deterministic blind models. Conversely, we prove that velocity-based parameterizations are inherently stable because they satisfy a bounded-gain condition that absorbs posterior uncertainty into a smooth geometric drift.

### 🤖 AI 总结

**一句话总结**：本文从几何与能量视角解释了为何无需显式噪声条件的“自洽/盲”扩散模型依然可以稳定采样，并本质上在执行对边缘能量的黎曼梯度流。

**研究动机**：现有盲扩散和Equilibrium Matching等噪声无关模型在实践上效果良好，但理论上存在两个悖论：一是当噪声水平是随机变量时究竟在优化什么能量景观，二是单一有界向量场在靠近数据流形处如何避免梯度发散并保持采样稳定。

**核心方法**：作者形式化定义了对所有噪声水平加权积分得到的“边缘能量”E_marg，并证明噪声无关模型学习到的是在一个局部共形度量下对该能量进行的黎曼梯度流；同时通过相对能量分解分析奇异性被度量精确抵消的机制，并对不同参数化（噪声预测 vs 速度预测）建立增益与稳定性条件。

**主要结论**：1）自主/盲扩散并非简单盲去噪，而是在边缘能量上的几何梯度流；2）原始能量在法向方向具1/t^p奇异势阱，但学习到的时间不变向量场隐式引入的共形度量可将其转化为稳定吸引子；3）噪声预测参数化存在“Jensen Gap”，使估计误差被高增益放大，导致确定性盲模型灾难性失效；4）速度参数化满足有界增益条件，可将后验不确定性吸收到平滑漂移项中，因此天然更稳定。

**关键词**：扩散模型, 生成模型, 向量场学习, 噪声无关建模, 边缘能量函数, 黎曼梯度流, 稳定采样理论, 速度参数化, autonomous

**评分**：36

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18428v1) | [下载PDF](https://arxiv.org/pdf/2602.18428v1.pdf)

---

## [20. Unifying approach to uniform expressivity of graph neural networks](https://arxiv.org/abs/2602.18409v1)

**作者**：Huan Luo, Jonni Virtema  
**分类**：cs.LG, cs.AI, cs.LO  
**发布时间**：2026-02-20

### 📄 论文摘要

The expressive power of Graph Neural Networks (GNNs) is often analysed via correspondence to the Weisfeiler-Leman (WL) algorithm and fragments of first-order logic. Standard GNNs are limited to performing aggregation over immediate neighbourhoods or over global read-outs. To increase their expressivity, recent attempts have been made to incorporate substructural information (e.g. cycle counts and subgraph properties). In this paper, we formalize this architectural trend by introducing Template GNNs (T-GNNs), a generalized framework where node features are updated by aggregating over valid template embeddings from a specified set of graph templates. We propose a corresponding logic, Graded template modal logic (GML(T)), and generalized notions of template-based bisimulation and WL algorithm. We establish an equivalence between the expressive power of T-GNNs and GML(T), and provide a unifying approach for analysing GNN expressivity: we show how standard AC-GNNs and its recent variants can be interpreted as instantiations of T-GNNs.

### 🤖 AI 总结

**一句话总结**：论文提出模板GNN（T-GNN）及其对应逻辑框架，统一刻画并提升图神经网络的表达能力。

**研究动机**：现有GNN多局限于局部邻居或全局读出，对复杂子结构（如环、特定子图）表达力不足，且缺乏统一的理论分析框架。

**核心方法**：作者引入以“图模板”为单位聚合信息的T-GNN框架，并提出对应的分级模板模态逻辑GML(T)、模板双模拟与模板版WL算法，建立T-GNN与GML(T)在表达能力上的等价。

**主要结论**：T-GNN为GNN的子结构增强提供了统一描述与分析工具，证明了其逻辑表达力并展示了标准AC-GNN及若干变体都可视为T-GNN实例，从而统一了多种提升GNN表达力的架构设计。

**关键词**：图神经网络, 深度学习, 神经网络表达能力, 模板GNN, T-GNN框架, 图结构子图匹配, 图同构测试, 逻辑可表达性分析, Weisfeiler-Leman算法, 子结构感知表示学习, ml

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18409v1) | [下载PDF](https://arxiv.org/pdf/2602.18409v1.pdf)

---

## [21. Scientific Knowledge-Guided Machine Learning for Vessel Power Prediction: A Comparative Study](https://arxiv.org/abs/2602.18403v1)

**作者**：Orfeas Bourchas, George Papalambrou  
**分类**：cs.LG  
**发布时间**：2026-02-20

### 📄 论文摘要

Accurate prediction of main engine power is essential for vessel performance optimization, fuel efficiency, and compliance with emission regulations. Conventional machine learning approaches, such as Support Vector Machines, variants of Artificial Neural Networks (ANNs), and tree-based methods like Random Forests, Extra Tree Regressors, and XGBoost, can capture nonlinearities but often struggle to respect the fundamental propeller law relationship between power and speed, resulting in poor extrapolation outside the training envelope. This study introduces a hybrid modeling framework that integrates physics-based knowledge from sea trials with data-driven residual learning. The baseline component, derived from calm-water power curves of the form $P = cV^n$, captures the dominant power-speed dependence, while another, nonlinear, regressor is then trained to predict the residual power, representing deviations caused by environmental and operational conditions. By constraining the machine learning task to residual corrections, the hybrid model simplifies learning, improves generalization, and ensures consistency with the underlying physics. In this study, an XGBoost, a simple Neural Network, and a Physics-Informed Neural Network (PINN) coupled with the baseline component were compared to identical models without the baseline component. Validation on in-service data demonstrates that the hybrid model consistently outperformed a pure data-driven baseline in sparse data regions while maintaining similar performance in populated ones. The proposed framework provides a practical and computationally efficient tool for vessel performance monitoring, with applications in weather routing, trim optimization, and energy efficiency planning.

### 🤖 AI 总结

**一句话总结**：本文提出一种将物理推进定律与数据驱动残差学习相结合的混合模型，用于更准确且可外推的船舶主机功率预测。

**研究动机**：传统纯机器学习模型虽能拟合非线性，但难以保证满足功率-航速的螺旋桨定律，在训练数据稀疏区间外推性能差，影响船舶节能与排放合规。

**核心方法**：先利用静水试航得到形如 P=cV^n 的物理基线模型，再用XGBoost、简单神经网络和PINN等模型仅学习“实测功率−基线功率”的残差，实现物理约束下的非线性修正，并与不含基线的纯数据驱动版本进行对比。

**主要结论**：在实船运营数据验证中，物理引导的混合模型在数据稀疏区域显著优于纯数据驱动模型，在数据密集区域性能相当，且具有良好物理一致性与计算效率，适用于船舶性能监测与能效优化决策。

**关键词**：机器学习, 人工神经网络, 物理信息神经网络, 集成学习, XGBoost, 船舶能效预测, 残差学习, 混合建模, 航行工况建模, 功率曲线拟合, machine learning

**评分**：24

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18403v1) | [下载PDF](https://arxiv.org/pdf/2602.18403v1.pdf)

---

## [22. Leakage and Second-Order Dynamics Improve Hippocampal RNN Replay](https://arxiv.org/abs/2602.18401v1)

**作者**：Josue Casco-Rodriguez, Nanda H. Krishna, Richard G. Baraniuk  
**分类**：cs.LG, cs.AI, q-bio.NC, stat.ML  
**发布时间**：2026-02-20

### 📄 论文摘要

Biological neural networks (like the hippocampus) can internally generate "replay" resembling stimulus-driven activity. Recent computational models of replay use noisy recurrent neural networks (RNNs) trained to path-integrate. Replay in these networks has been described as Langevin sampling, but new modifiers of noisy RNN replay have surpassed this description. We re-examine noisy RNN replay as sampling to understand or improve it in three ways: (1) Under simple assumptions, we prove that the gradients replay activity should follow are time-varying and difficult to estimate, but readily motivate the use of hidden state leakage in RNNs for replay. (2) We confirm that hidden state adaptation (negative feedback) encourages exploration in replay, but show that it incurs non-Markov sampling that also slows replay. (3) We propose the first model of temporally compressed replay in noisy path-integrating RNNs through hidden state momentum, connect it to underdamped Langevin sampling, and show that, together with adaptation, it counters slowness while maintaining exploration. We verify our findings via path-integration of 2D triangular and T-maze paths and of high-dimensional paths of synthetic rat place cell activity.

### 🤖 AI 总结

**一句话总结**：论文通过在噪声RNN中引入隐藏态泄露与二阶动力学（动量），系统性改进了类海马体的路径重放质量与速度，并用采样视角统一解释这些机制。

**研究动机**：现有将海马体重放建模为噪声RNN的工作多用Langevin采样解释，但难以说明为何加入泄露、适应等修饰会显著改变重放特性，因此需要从严格的采样与动力学角度重新分析并设计更高效的重放机制。

**核心方法**：作者将路径积分RNN的重放形式化为时间变化的采样过程，理论推导出理想重放的梯度性质，进而引入隐藏态泄露、负反馈适应与隐藏态动量（类欠阻尼Langevin），并在2D迷宫与高维位置细胞活动路径上系统实验验证对探索性、速度与时间压缩的影响。

**主要结论**：（1）理想重放对应的梯度是时变且难估计，但自然指向在RNN中加入隐藏态泄露；（2）隐藏态适应能促进状态空间探索，却引入非马尔可夫性并减慢重放；（3）加入隐藏态动量可实现时间压缩式重放，并与适应互补，在保持探索性的同时显著加快重放，为类海马体RNN重放提供了统一的二阶动力学采样框架。

**关键词**：深度学习, 神经网络, 循环神经网络RNN, 噪声RNN, 序列建模, 轨迹重放, 路径积分, 神经表征学习, 海马体启发模型, neural network

**评分**：16

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18401v1) | [下载PDF](https://arxiv.org/pdf/2602.18401v1.pdf)

---

## [23. PRISM-FCP: Byzantine-Resilient Federated Conformal Prediction via Partial Sharing](https://arxiv.org/abs/2602.18396v1)

**作者**：Ehsan Lari, Reza Arablouei, Stefan Werner  
**分类**：cs.LG, eess.SP, math.PR, stat.AP, stat.ML  
**发布时间**：2026-02-20

### 📄 论文摘要

We propose PRISM-FCP (Partial shaRing and robust calIbration with Statistical Margins for Federated Conformal Prediction), a Byzantine-resilient federated conformal prediction framework that utilizes partial model sharing to improve robustness against Byzantine attacks during both model training and conformal calibration. Existing approaches address adversarial behavior only in the calibration stage, leaving the learned model susceptible to poisoned updates. In contrast, PRISM-FCP mitigates attacks end-to-end. During training, clients partially share updates by transmitting only $M$ of $D$ parameters per round. This attenuates the expected energy of an adversary's perturbation in the aggregated update by a factor of $M/D$, yielding lower mean-square error (MSE) and tighter prediction intervals. During calibration, clients convert nonconformity scores into characterization vectors, compute distance-based maliciousness scores, and downweight or filter suspected Byzantine contributions before estimating the conformal quantile. Extensive experiments on both synthetic data and the UCI Superconductivity dataset demonstrate that PRISM-FCP maintains nominal coverage guarantees under Byzantine attacks while avoiding the interval inflation observed in standard FCP with reduced communication, providing a robust and communication-efficient approach to federated uncertainty quantification.

### 🤖 AI 总结

**一句话总结**：PRISM-FCP 提出了一种在训练与校准两阶段均具拜占庭鲁棒性的联邦共形预测框架，通过部分参数共享与鲁棒量化确保在攻击下仍保持有效置信区间。

**研究动机**：现有联邦共形预测方法通常只在校准阶段防御恶意客户端，导致训练得到的模型易被投毒且置信区间在攻击下严重膨胀，缺乏端到端的鲁棒不确定性量化能力。

**核心方法**：在训练阶段，PRISM-FCP 每轮仅从 D 个参数中随机共享 M 个，使恶意扰动在聚合中的能量缩小约 M/D，从而降低 MSE；在校准阶段，将非一致性评分转换为表征向量，基于距离计算“恶意度”并对可疑客户端的贡献进行降权或过滤后再估计共形分位数。

**主要结论**：在合成数据及 UCI Superconductivity 数据集上的实验表明，PRISM-FCP 在存在拜占庭攻击时仍能维持名义覆盖率，避免标准 FCP 置信区间膨胀，并同时实现鲁棒性与通信效率的平衡。

**关键词**：联邦学习, 机器学习, 深度学习, 分布式训练, 对抗鲁棒性, 拜占庭容错, 不确定性量化, 保序预测, 参数部分共享, 恶意客户端检测, rag

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18396v1) | [下载PDF](https://arxiv.org/pdf/2602.18396v1.pdf)

---

## [24. FedZMG: Efficient Client-Side Optimization in Federated Learning](https://arxiv.org/abs/2602.18384v1)

**作者**：Fotios Zantalis, Evangelos Zervas, Grigorios Koulouras  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-20

### 📄 论文摘要

Federated Learning (FL) enables distributed model training on edge devices while preserving data privacy. However, clients tend to have non-Independent and Identically Distributed (non-IID) data, which often leads to client-drift, and therefore diminishing convergence speed and model performance. While adaptive optimizers have been proposed to mitigate these effects, they frequently introduce computational complexity or communication overhead unsuitable for resource-constrained IoT environments. This paper introduces Federated Zero Mean Gradients (FedZMG), a novel, parameter-free, client-side optimization algorithm designed to tackle client-drift by structurally regularizing the optimization space. Advancing the idea of Gradient Centralization, FedZMG projects local gradients onto a zero-mean hyperplane, effectively neutralizing the "intensity" or "bias" shifts inherent in heterogeneous data distributions without requiring additional communication or hyperparameter tuning. A theoretical analysis is provided, proving that FedZMG reduces the effective gradient variance and guarantees tighter convergence bounds compared to standard FedAvg. Extensive empirical evaluations on EMNIST, CIFAR100, and Shakespeare datasets demonstrate that FedZMG achieves better convergence speed and final validation accuracy compared to the baseline FedAvg and the adaptive optimizer FedAdam, particularly in highly non-IID settings.

### 🤖 AI 总结

**一句话总结**：FedZMG 提出一种在联邦学习客户端侧进行零均值梯度投影的无参数优化方法，在非IID数据下兼顾高效性与更快收敛。

**研究动机**：现有联邦学习在非IID数据下存在严重client-drift问题，而诸多自适应优化器虽能缓解但计算与通信开销过大，不适用于资源受限的边缘/物联网设备。

**核心方法**：FedZMG 在本地训练时对梯度进行“零均值超平面”投影（基于梯度中心化思想），通过去除梯度中的全局偏移成分来降低有效梯度方差，无需额外通信或超参数调节，并给出收敛性理论分析。

**主要结论**：在 EMNIST、CIFAR100 和 Shakespeare 等数据集的高度非IID场景中，FedZMG 相比 FedAvg 与 FedAdam 实验上表现出更快的收敛速度和更高的最终验证精度，并在理论上证明其具有更紧的收敛界。

**关键词**：联邦学习, 机器学习, 深度学习, 边缘计算, 客户端优化, 梯度集中化, FedZMG算法, 非IID数据, 收敛性分析, 物联网场景, agent

**评分**：21

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18384v1) | [下载PDF](https://arxiv.org/pdf/2602.18384v1.pdf)

---

## [25. Explaining AutoClustering: Uncovering Meta-Feature Contribution in AutoML for Clustering](https://arxiv.org/abs/2602.18348v1)

**作者**：Matheus Camilo da Silva, Leonardo Arrighi, Ana Carolina Lorena 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-20

### 📄 论文摘要

AutoClustering methods aim to automate unsupervised learning tasks, including algorithm selection (AS), hyperparameter optimization (HPO), and pipeline synthesis (PS), by often leveraging meta-learning over dataset meta-features. While these systems often achieve strong performance, their recommendations are often difficult to justify: the influence of dataset meta-features on algorithm and hyperparameter choices is typically not exposed, limiting reliability, bias diagnostics, and efficient meta-feature engineering. This limits reliability and diagnostic insight for further improvements. In this work, we investigate the explainability of the meta-models in AutoClustering. We first review 22 existing methods and organize their meta-features into a structured taxonomy. We then apply a global explainability technique (i.e., Decision Predicate Graphs) to assess feature importance within meta-models from selected frameworks. Finally, we use local explainability tools such as SHAP (SHapley Additive exPlanations) to analyse specific clustering decisions. Our findings highlight consistent patterns in meta-feature relevance, identify structural weaknesses in current meta-learning strategies that can distort recommendations, and provide actionable guidance for more interpretable Automated Machine Learning (AutoML) design. This study therefore offers a practical foundation for increasing decision transparency in unsupervised learning automation.

### 🤖 AI 总结

**一句话总结**：本文系统梳理AutoClustering中的数据集元特征，并用可解释性技术分析这些元特征如何影响自动聚类算法与超参数推荐，从而提升AutoML决策透明度。

**研究动机**：现有AutoClustering虽然能自动完成算法选择和超参搜索，但其基于元特征的决策过程不透明，难以诊断偏差、改进元特征工程或提升系统可靠性。

**核心方法**：作者综述并归类22种方法中的数据集元特征，构建元特征分类体系；在选定框架上用全局解释方法（Decision Predicate Graphs）分析元模型的特征重要性，并结合局部解释工具SHAP深入剖析具体聚类决策。

**主要结论**：结果表明不同方法在元特征重要性上存在稳定模式，也暴露出当前元学习策略中可能导致推荐偏差的结构性问题，并据此提出更可解释的AutoML/AutoClustering设计建议，为提升无监督自动化学习的决策透明度提供实践基础。

**关键词**：机器学习, 深度学习, 神经网络, AutoML自动机器学习, 无监督学习聚类, 算法选择AS, 超参数优化HPO, 元学习meta-learning, 模型可解释性, 特征重要性分析, SHAP解释方法, 决策谓词图DPG

**评分**：21

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18348v1) | [下载PDF](https://arxiv.org/pdf/2602.18348v1.pdf)

---

## [26. On the "Induction Bias" in Sequence Models](https://arxiv.org/abs/2602.18333v1)

**作者**：M. Reza Ebrahimi, Michaël Defferrard, Sunny Panchal 等 4 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-02-20

### 📄 论文摘要

Despite the remarkable practical success of transformer-based language models, recent work has raised concerns about their ability to perform state tracking. In particular, a growing body of literature has shown this limitation primarily through failures in out-of-distribution (OOD) generalization, such as length extrapolation. In this work, we shift attention to the in-distribution implications of these limitations. We conduct a large-scale experimental study of the data efficiency of transformers and recurrent neural networks (RNNs) across multiple supervision regimes. We find that the amount of training data required by transformers grows much more rapidly with state-space size and sequence length than for RNNs. Furthermore, we analyze the extent to which learned state-tracking mechanisms are shared across different sequence lengths. We show that transformers exhibit negligible or even detrimental weight sharing across lengths, indicating that they learn length-specific solutions in isolation. In contrast, recurrent models exhibit effective amortized learning by sharing weights across lengths, allowing data from one sequence length to improve performance on others. Together, these results demonstrate that state tracking remains a fundamental challenge for transformers, even when training and evaluation distributions match.

### 🤖 AI 总结

**一句话总结**：论文系统比较了Transformer与RNN在状态跟踪任务上的归纳偏置，发现Transformer即便在分布内也明显不如RNN数据高效，且难以在不同序列长度之间共享已学到的状态跟踪机制。

**研究动机**：现有批评多集中在Transformer在长度外推等OOD场景中的失败，这篇工作关注：在训练和测试分布一致时，Transformer在状态跟踪方面是否仍存在根本性局限，并与RNN的归纳偏置差异何在。

**核心方法**：作者构造多种需要显式状态跟踪的序列任务，在多种监督设定下，系统比较Transformer与RNN的样本复杂度（随状态空间大小与序列长度变化），并通过跨长度训练/测试分析模型在不同序列长度上的权重共享和“摊还学习”能力。

**主要结论**：Transformer在状态空间规模和序列长度增大时，所需训练数据增长远快于RNN，且其学到的解强烈依赖具体长度，跨长度权重共享甚微甚至有负效应；而RNN则能有效复用参数进行摊还学习，说明即使在分布内，状态跟踪仍是Transformer的根本挑战。

**关键词**：深度学习, transformer, 神经网络, 序列建模, 状态跟踪, 长度外推, 数据效率, 监督学习, 长度泛化, 权重共享

**评分**：24

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18333v1) | [下载PDF](https://arxiv.org/pdf/2602.18333v1.pdf)

---

## [27. JPmHC Dynamical Isometry via Orthogonal Hyper-Connections](https://arxiv.org/abs/2602.18308v1)

**作者**：Biswa Sengupta, Jinhua Wang, Leo Brunswic  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-20

### 📄 论文摘要

Recent advances in deep learning, exemplified by Hyper-Connections (HC), have expanded the residual connection paradigm by introducing wider residual streams and diverse connectivity patterns. While these innovations yield significant performance gains, they compromise the identity mapping property of residual connections, leading to training instability, limited scalability, and increased memory overhead. To address these challenges, we propose JPmHC (Jacobian-spectrum Preserving manifold-constrained Hyper-Connections), a framework that replaces identity skips with a trainable linear mixer acting on n parallel streams while explicitly controlling gradient conditioning. By constraining the mixer M on operator-norm-bounded manifolds (e.g., bistochastic, Stiefel, Grassmann), JPmHC prevents gradient pathologies and enhances stability. JPmHC introduces three key contributions: (i) a free-probability analysis that predicts Jacobian spectra for structured skips, providing actionable design rules for mixer selection; (ii) memory-efficient implicit differentiation for fixed-point projections, reducing activation memory and synchronization overhead; and (iii) a Stiefel-constrained mixer via Cayley transforms, ensuring orthogonality without post-hoc normalization. Empirical evaluations on ARC-AGI demonstrate that JPmHC achieves faster convergence, higher accuracy, and lower computational cost compared to bistochastic baselines. As a flexible and scalable extension of HC, JPmHC advances spectrum-aware, stable, and efficient deep learning, offering insights into topological architecture design and foundational model evolution.

### 🤖 AI 总结

**一句话总结**：论文提出JPmHC框架，用受约束的可训练线性混合器替代传统残差/Hyper-Connections中的恒等跳连，在保持良好Jacobian谱的同时提升训练稳定性与效率。

**研究动机**：现有Hyper-Connections虽然通过更宽和更复杂的残差流提升性能，但破坏了恒等映射特性，导致梯度不稳定、难以扩展、内存开销大，因此需要一种既保持谱良好又可扩展的连接机制。

**核心方法**：将n路并行残差流通过受流形约束的线性混合器M（如双随机、Stiefel、Grassmann）进行组合，利用自由概率分析预测并设计Jacobian谱，用隐式微分提升投影计算的内存效率，并通过Cayley变换实现Stiefel约束下的正交混合器。

**主要结论**：在ARC-AGI等任务上，JPmHC相较双随机基线实现更快收敛、更高精度和更低计算成本，展示出作为一种可扩展、谱感知且稳定高效的Hyper-Connection扩展形式，对拓扑化网络结构设计和基础模型演化具有启发意义。

**关键词**：深度学习, 神经网络, 残差连接, 超连接架构, 正交约束, Stiefel流形, Cayley变换, 谱归一化, 稳定训练, 高效梯度传播, deep learning

**评分**：20

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18308v1) | [下载PDF](https://arxiv.org/pdf/2602.18308v1.pdf)

---

## [28. Analyzing and Improving Chain-of-Thought Monitorability Through Information Theory](https://arxiv.org/abs/2602.18297v1)

**作者**：Usman Anwar, Tim Bakker, Dana Kianfar 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.CL, cs.IT  
**发布时间**：2026-02-20

### 📄 论文摘要

Chain-of-thought (CoT) monitors are LLM-based systems that analyze reasoning traces to detect when outputs may exhibit attributes of interest, such as test-hacking behavior during code generation. In this paper, we use information-theoretic analysis to show that non-zero mutual information between CoT and output is a necessary but not sufficient condition for CoT monitorability. We identify two sources of approximation error that may undermine the performance of CoT monitors in practice: information gap, which measures the extent to which the monitor can extract the information available in CoT, and elicitation error, which measures the extent to which the monitor approximates the optimal monitoring function. We further demonstrate that CoT monitorability can be systematically improved through targeted training objectives. To this end, we propose two complementary approaches: (a) an oracle-based method that directly rewards the monitored model for producing CoTs that maximize monitor accuracy, and (b) a more practical, label-free approach that maximizes conditional mutual information between outputs and CoTs. Across multiple different environments, we show both methods significantly improve monitor accuracy while preventing CoT degeneration even when training against a monitor, thereby mitigating reward hacking when the task reward is imperfectly specified.

### 🤖 AI 总结

**一句话总结**：本文用信息论形式化分析“思维链监控”的可监控性条件，并通过新训练目标显著提升监控器在防止奖励黑客等场景中的有效性。

**研究动机**：现有基于思维链（CoT）的监控器虽能查看推理过程，但缺乏对“何时、在何种条件下”这些 CoT 真正有助于可靠监控的理论理解，也缺乏系统提升可监控性的训练方法。

**核心方法**：作者用互信息形式化 CoT 与输出之间的信息关系，提出“信息缺口”和“引出误差”两类近似误差，并设计两种提升方案：一是基于“监督者（oracle）”的训练，直接奖励模型生成能最大化监控准确率的 CoT；二是无需标签、最大化输出与 CoT 条件互信息的训练目标。

**主要结论**：信息论分析表明：CoT 与输出存在非零互信息是可监控的必要非充分条件，而实际监控性能受限于信息缺口与引出误差；通过提出的有监督与无监督两种目标优化 CoT，可在多种环境下显著提升监控准确率、避免 CoT 退化，并在奖励不完美设定时有效缓解奖励黑客问题。

**关键词**：大语言模型, 链式思维, transformer, 信息论分析, 互信息优化, 监控模型训练, 测试规避检测, 代码生成安全, 奖励黑客防护

**评分**：52

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18297v1) | [下载PDF](https://arxiv.org/pdf/2602.18297v1.pdf)

---

## [29. PRISM: Parallel Reward Integration with Symmetry for MORL](https://arxiv.org/abs/2602.18277v1)

**作者**：Finn van der Knaap, Kejiang Qian, Zheng Xu 等 4 位作者  
**分类**：cs.LG, cs.AI, stat.ML  
**发布时间**：2026-02-20

### 📄 论文摘要

This work studies heterogeneous Multi-Objective Reinforcement Learning (MORL), where objectives can differ sharply in temporal frequency. Such heterogeneity allows dense objectives to dominate learning, while sparse long-horizon rewards receive weak credit assignment, leading to poor sample efficiency. We propose a Parallel Reward Integration with Symmetry (PRISM) algorithm that enforces reflectional symmetry as an inductive bias in aligning reward channels. PRISM introduces ReSymNet, a theory-motivated model that reconciles temporal-frequency mismatches across objectives, using residual blocks to learn a scaled opportunity value that accelerates exploration while preserving the optimal policy. We also propose SymReg, a reflectional equivariance regulariser that enforces agent mirroring and constrains policy search to a reflection-equivariant subspace. This restriction provably reduces hypothesis complexity and improves generalisation. Across MuJoCo benchmarks, PRISM consistently outperforms both a sparse-reward baseline and an oracle trained with full dense rewards, improving Pareto coverage and distributional balance: it achieves hypervolume gains exceeding 100\% over the baseline and up to 32\% over the oracle. The code is at \href{https://github.com/EVIEHub/PRISM}{https://github.com/EVIEHub/PRISM}.

### 🤖 AI 总结

**一句话总结**：PRISM通过并行奖励整合与反射对称归纳偏置，解决多目标强化学习中稀疏与稠密奖励频率不匹配导致的训练失衡问题。

**研究动机**：在多目标强化学习中，不同目标的时间频率差异会导致稠密奖励主导学习、稀疏长时序目标难以获得有效回传，造成样本效率低和多目标性能不均衡。

**核心方法**：提出PRISM框架，引入ReSymNet通过残差结构学习“缩放的机会值”以对齐不同频率的奖励通道并加速探索，同时设计对称等变正则SymReg强制策略满足空间反射对称性，从而压缩假设空间并提升泛化能力。

**主要结论**：在MuJoCo多目标基准上，PRISM相较稀疏奖励基线和使用完整稠密奖励的oracle均取得显著优势，在Pareto覆盖度和分布平衡上有明显提升，超体积指标相对基线提高超过100%、相对oracle最高提高约32%。

**关键词**：强化学习, 多目标强化学习, 深度学习, agent, 奖励建模, 对称性正则, 策略优化, 探索效率, MuJoCo仿真环境, Pareto前沿

**评分**：40

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18277v1) | [下载PDF](https://arxiv.org/pdf/2602.18277v1.pdf)

---

## [30. A Probabilistic Framework for LLM-Based Model Discovery](https://arxiv.org/abs/2602.18266v1)

**作者**：Stefan Wahl, Raphaela Schenk, Ali Farnoud 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-20

### 📄 论文摘要

Automated methods for discovering mechanistic simulator models from observational data offer a promising path toward accelerating scientific progress. Such methods often take the form of agentic-style iterative workflows that repeatedly propose and revise candidate models by imitating human discovery processes. However, existing LLM-based approaches typically implement such workflows via hand-crafted heuristic procedures, without an explicit probabilistic formulation. We recast model discovery as probabilistic inference, i.e., as sampling from an unknown distribution over mechanistic models capable of explaining the data. This perspective provides a unified way to reason about model proposal, refinement, and selection within a single inference framework. As a concrete instantiation of this view, we introduce ModelSMC, an algorithm based on Sequential Monte Carlo sampling. ModelSMC represents candidate models as particles which are iteratively proposed and refined by an LLM, and weighted using likelihood-based criteria. Experiments on real-world scientific systems illustrate that this formulation discovers models with interpretable mechanisms and improves posterior predictive checks. More broadly, this perspective provides a probabilistic lens for understanding and developing LLM-based approaches to model discovery.

### 🤖 AI 总结

**一句话总结**：论文将利用LLM进行机理模型发现的问题形式化为一次概率推断过程，并提出基于顺序蒙特卡洛的ModelSMC框架来统一处理模型生成、修正与选择。

**研究动机**：现有基于LLM的科学模型发现多依赖手工设计的启发式“智能体式”工作流，缺乏统一的概率视角，难以系统性评估和改进模型生成与选择过程。

**核心方法**：作者将“发现机理模型”视为从能解释观测数据的模型后验分布中采样，引入ModelSMC算法：把候选模型视为粒子，由LLM迭代生成与改写，并通过似然相关的权重进行评估与重采样，从而实现概率化的模型搜索与精炼。

**主要结论**：在真实科学系统上的实验表明，ModelSMC能发现具有可解释机理的模型并提升后验预测检验表现，同时该概率框架为设计和分析LLM驱动的模型发现方法提供了统一的理论视角。

**关键词**：大语言模型, LLM, agentic workflow, 模型发现, 概率推理, Sequential Monte Carlo, 模型生成与改进, 科学机制建模, 后验预测检查

**评分**：41

**论文链接**：[查看原文](https://arxiv.org/abs/2602.18266v1) | [下载PDF](https://arxiv.org/pdf/2602.18266v1.pdf)

---

