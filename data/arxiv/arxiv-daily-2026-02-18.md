# arXiv AI 论文日报 | 2026-02-18

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.LG](#csLG) (9 篇)
- [cs.CV](#csCV) (10 篇)
- [cs.AI](#csAI) (3 篇)
- [cs.CL](#csCL) (8 篇)

---

## cs.AI

## [1. Developing AI Agents with Simulated Data: Why, what, and how?](https://arxiv.org/abs/2602.15816v1)

**作者**：Xiaoran Liu, Istvan David  
**分类**：cs.AI, cs.ET  
**发布时间**：2026-02-17

### 📄 论文摘要

As insufficient data volume and quality remain the key impediments to the adoption of modern subsymbolic AI, techniques of synthetic data generation are in high demand. Simulation offers an apt, systematic approach to generating diverse synthetic data. This chapter introduces the reader to the key concepts, benefits, and challenges of simulation-based synthetic data generation for AI training purposes, and to a reference framework to describe, design, and analyze digital twin-based AI simulation solutions.

### 🤖 AI 总结

**一句话总结**：本文系统梳理了用仿真生成合成数据来训练AI代理的动机、关键概念与挑战，并提出一个基于数字孪生的参考框架。

**研究动机**：现实世界数据在规模、标注质量、覆盖极端场景与安全性方面存在显著不足，限制了现代子符号AI（如深度学习与智能体）在复杂任务中的应用，因此需要可控、可扩展的仿真环境来生成高质量合成数据。

**核心方法**：作者提出以数字孪生为基础的仿真建模思路，定义仿真要素（环境、实体、交互、任务等）及其配置方式，并给出一个用于描述、设计和分析AI仿真系统的参考框架，以系统性地构建用于训练与评估AI代理的合成数据管线。

**主要结论**：仿真驱动的合成数据是缓解数据瓶颈、提升AI代理泛化性与安全性的有力途径，但仍需在仿真逼真度、域迁移差距、成本与验证方法上持续研究，数字孪生参考框架为相关系统的工程化设计提供了统一语言和指导。

**关键词**：机器学习, 深度学习, 神经网络, AI代理, 多智能体, 数字孪生仿真, 合成数据生成, 仿真环境构建, 模拟训练数据, 模型泛化能力

**评分**：39

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15816v1) | [下载PDF](https://arxiv.org/pdf/2602.15816v1.pdf)

---

## [2. Enhancing Building Semantics Preservation in AI Model Training with Large Language Model Encodings](https://arxiv.org/abs/2602.15791v1)

**作者**：Suhyung Jang, Ghang Lee, Jaekun Lee 等 4 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-02-17

### 📄 论文摘要

Accurate representation of building semantics, encompassing both generic object types and specific subtypes, is essential for effective AI model training in the architecture, engineering, construction, and operation (AECO) industry. Conventional encoding methods (e.g., one-hot) often fail to convey the nuanced relationships among closely related subtypes, limiting AI's semantic comprehension. To address this limitation, this study proposes a novel training approach that employs large language model (LLM) embeddings (e.g., OpenAI GPT and Meta LLaMA) as encodings to preserve finer distinctions in building semantics. We evaluated the proposed method by training GraphSAGE models to classify 42 building object subtypes across five high-rise residential building information models (BIMs). Various embedding dimensions were tested, including original high-dimensional LLM embeddings (1,536, 3,072, or 4,096) and 1,024-dimensional compacted embeddings generated via the Matryoshka representation model. Experimental results demonstrated that LLM encodings outperformed the conventional one-hot baseline, with the llama-3 (compacted) embedding achieving a weighted average F1-score of 0.8766, compared to 0.8475 for one-hot encoding. The results underscore the promise of leveraging LLM-based encodings to enhance AI's ability to interpret complex, domain-specific building semantics. As the capabilities of LLMs and dimensionality reduction techniques continue to evolve, this approach holds considerable potential for broad application in semantic elaboration tasks throughout the AECO industry.

### 🤖 AI 总结

**一句话总结**：论文提出用大模型语义向量取代传统独热编码来表示建筑构件语义，在BIM下游分类任务中显著提升了细粒度子类别识别效果。

**研究动机**：传统one-hot等编码无法表达建筑构件子类型之间的细腻语义关系，限制了AECO场景中AI模型对复杂建筑语义的理解与泛化能力。

**核心方法**：将建筑对象类型/子类型文本输入LLM（如GPT、LLaMA）获取高维语义embedding，并结合Matryoshka降维生成紧凑向量，作为GraphSAGE节点特征，对五个高层住宅BIM中的42类建筑对象子类型进行分类训练与对比实验。

**主要结论**：LLM语义编码在加权F1上明显优于one-hot（如压缩后的llama-3 embedding达0.8766，对比0.8475），证明利用LLM embedding可更好保留建筑领域细粒度语义，未来有潜力广泛应用于AECO行业的各类语义细化与理解任务。

**关键词**：大语言模型, LLM嵌入, embedding, 图神经网络, GraphSAGE, 建筑语义建模, BIM语义分类, 高层住宅建筑, 特征降维, 表示学习

**评分**：36

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15791v1) | [下载PDF](https://arxiv.org/pdf/2602.15791v1.pdf)

---

## [3. GlobeDiff: State Diffusion Process for Partial Observability in Multi-Agent Systems](https://arxiv.org/abs/2602.15776v1)

**作者**：Yiqin Yang, Xu Yang, Yuhua Jiang 等 11 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-17

### 📄 论文摘要

In the realm of multi-agent systems, the challenge of \emph{partial observability} is a critical barrier to effective coordination and decision-making. Existing approaches, such as belief state estimation and inter-agent communication, often fall short. Belief-based methods are limited by their focus on past experiences without fully leveraging global information, while communication methods often lack a robust model to effectively utilize the auxiliary information they provide. To solve this issue, we propose Global State Diffusion Algorithm~(GlobeDiff) to infer the global state based on the local observations. By formulating the state inference process as a multi-modal diffusion process, GlobeDiff overcomes ambiguities in state estimation while simultaneously inferring the global state with high fidelity. We prove that the estimation error of GlobeDiff under both unimodal and multi-modal distributions can be bounded. Extensive experimental results demonstrate that GlobeDiff achieves superior performance and is capable of accurately inferring the global state.

### 🤖 AI 总结

**一句话总结**：GlobeDiff将多智能体部分可观测环境中的全局状态推断建模为多模态扩散过程，从局部观测中高保真恢复环境全局状态。

**研究动机**：现有基于信念状态或通信的多智能体方法，要么只依赖历史经验、未充分利用潜在的全局信息，要么缺乏系统化模型来有效利用辅助通信信息，导致在部分可观测环境下全局状态估计不准确。

**核心方法**：提出Global State Diffusion Algorithm（GlobeDiff），将从局部观测推断全局状态视为多模态扩散生成过程，通过扩散模型消除状态估计歧义并给出全局状态重建；理论上对单峰和多峰分布下的估计误差给出上界。

**主要结论**：实验表明，GlobeDiff在多智能体部分可观测任务中显著优于现有方法，能够稳定、准确地重构全局状态，并在理论上保证其估计误差可控。

**关键词**：多智能体系统, 深度学习, 扩散模型, 状态估计, 部分可观测环境, 多模态建模, 全局状态推断, 协同决策, agent

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15776v1) | [下载PDF](https://arxiv.org/pdf/2602.15776v1.pdf)

---

## cs.CL

## [4. *-PLUIE: Personalisable metric with Llm Used for Improved Evaluation](https://arxiv.org/abs/2602.15778v1)

**作者**：Quentin Lemesle, Léane Jourdan, Daisy Munson 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-02-17

### 📄 论文摘要

Evaluating the quality of automatically generated text often relies on LLM-as-a-judge (LLM-judge) methods. While effective, these approaches are computationally expensive and require post-processing. To address these limitations, we build upon ParaPLUIE, a perplexity-based LLM-judge metric that estimates confidence over ``Yes/No'' answers without generating text. We introduce *-PLUIE, task specific prompting variants of ParaPLUIE and evaluate their alignment with human judgement. Our experiments show that personalised *-PLUIE achieves stronger correlations with human ratings while maintaining low computational cost.

### 🤖 AI 总结

**一句话总结**：*-PLUIE在不生成文本的前提下，通过任务和个性化提示设计，用困惑度近似LLM裁判评分，并与人工评价高度相关。

**研究动机**：传统LLM-as-a-judge需要生成长文本、计算成本高且需额外后处理，因此需要一种更轻量但仍与人类判断高度一致的自动评价指标。

**核心方法**：在ParaPLUIE基于困惑度评估“Yes/No”答案置信度的框架上，设计面向不同任务和用户偏好的个性化提示变体（*-PLUIE），直接用语言模型的概率分布而非生成文本来打分。

**主要结论**：实验表明，个性化的*-PLUIE在保持低计算开销的同时，相比原始方法能获得更高的人类相关性，是更实用的自动文本质量评价指标。

**关键词**：大语言模型, LLM评估, 自动文本生成质量, 机器学习, perplexity度量, 人类偏好对齐, 个性化评估指标, 文本相关性打分, 模型判别器, 任务特定提示词设计

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15778v1) | [下载PDF](https://arxiv.org/pdf/2602.15778v1.pdf)

---

## [5. ViTaB-A: Evaluating Multimodal Large Language Models on Visual Table Attribution](https://arxiv.org/abs/2602.15769v1)

**作者**：Yahia Alqurnawi, Preetom Biswas, Anmol Rao 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-02-17

### 📄 论文摘要

Multimodal Large Language Models (mLLMs) are often used to answer questions in structured data such as tables in Markdown, JSON, and images. While these models can often give correct answers, users also need to know where those answers come from. In this work, we study structured data attribution/citation, which is the ability of the models to point to the specific rows and columns that support an answer. We evaluate several mLLMs across different table formats and prompting strategies. Our results show a clear gap between question answering and evidence attribution. Although question answering accuracy remains moderate, attribution accuracy is much lower, near random for JSON inputs, across all models. We also find that models are more reliable at citing rows than columns, and struggle more with textual formats than images. Finally, we observe notable differences across model families. Overall, our findings show that current mLLMs are unreliable at providing fine-grained, trustworthy attribution for structured data, which limits their usage in applications requiring transparency and traceability.

### 🤖 AI 总结

**一句话总结**：本文构建视觉表格溯源评测基准，系统评估多模态大模型在表格问答中的证据归因能力，发现其引用具体行列证据的表现远逊于回答准确率。

**研究动机**：实际应用中用户不仅要正确答案，还需知道答案在表格中的具体出处以实现可追溯和可信赖，但现有多模态大模型在结构化数据上的细粒度归因能力尚不清楚。

**核心方法**：作者构建ViTaB-A基准，在Markdown、JSON和表格图像等多种格式下，对多种多模态大模型在表格问答与“指出支持答案的具体行列”这两项任务上进行系统对比，并分析不同提示策略、行/列归因差异及模型家族差异。

**主要结论**：结果显示：虽然表格问答准确率中等，但证据归因几乎接近随机，尤其在JSON输入上最差；模型更擅长标注行而非列，对文本格式比图像更困难，不同模型家族存在明显差异，总体表明当前多模态大模型在结构化数据的精细溯源方面不可靠，限制了其在高透明度场景中的应用。

**关键词**：多模态大模型, 表格问答, 结构化数据归因, 证据定位, 可解释性, Markdown表格, JSON解析, 模型可靠性, ml

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15769v1) | [下载PDF](https://arxiv.org/pdf/2602.15769v1.pdf)

---

## [6. ChartEditBench: Evaluating Grounded Multi-Turn Chart Editing in Multimodal Language Models](https://arxiv.org/abs/2602.15758v1)

**作者**：Manav Nitin Kapadnis, Lawanya Baghel, Atharva Naik 等 4 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-02-17

### 📄 论文摘要

While Multimodal Large Language Models (MLLMs) perform strongly on single-turn chart generation, their ability to support real-world exploratory data analysis remains underexplored. In practice, users iteratively refine visualizations through multi-turn interactions that require maintaining common ground, tracking prior edits, and adapting to evolving preferences. We introduce ChartEditBench, a benchmark for incremental, visually grounded chart editing via code, comprising 5,000 difficulty-controlled modification chains and a rigorously human-verified subset. Unlike prior one-shot benchmarks, ChartEditBench evaluates sustained, context-aware editing. We further propose a robust evaluation framework that mitigates limitations of LLM-as-a-Judge metrics by integrating execution-based fidelity checks, pixel-level visual similarity, and logical code verification. Experiments with state-of-the-art MLLMs reveal substantial degradation in multi-turn settings due to error accumulation and breakdowns in shared context, with strong performance on stylistic edits but frequent execution failures on data-centric transformations. ChartEditBench, establishes a challenging testbed for grounded, intent-aware multimodal programming.

### 🤖 AI 总结

**一句话总结**：ChartEditBench提出了一个专门评估多模态大模型在多轮、可视化落地的图表编辑能力的新基准与评测框架。

**研究动机**：现有评测多集中在单轮图表生成，无法反映真实数据分析场景中多轮迭代、追踪历史编辑和适应用户偏好的能力，因此需要一个专门针对多轮图表编辑的基准。

**核心方法**：作者构建了包含5000条、难度可控的图表修改链及人工校验子集，并设计结合代码执行一致性、像素级视觉相似度和逻辑代码校验的综合评估框架，以系统测量MLLM在多轮图表编辑中的表现。

**主要结论**：实验发现当前最先进多模态大模型在多轮场景中因错误累积和上下文共享失败而性能明显下降，对风格类编辑表现尚可，但在数据相关变换上执行失败率高，ChartEditBench因而成为推动具备扎实语境与意图理解能力的多模态编程模型的重要挑战基准。

**关键词**：多模态大模型, LLM, 上下文跟踪, 意图感知交互, 可视化编辑, 代码生成评测, 多轮对话, 数据可视分析

**评分**：39

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15758v1) | [下载PDF](https://arxiv.org/pdf/2602.15758v1.pdf)

---

## [7. Beyond Binary Classification: Detecting Fine-Grained Sexism in Social Media Videos](https://arxiv.org/abs/2602.15757v1)

**作者**：Laura De Grazia, Danae Sánchez Villegas, Desmond Elliott 等 5 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-02-17

### 📄 论文摘要

Online sexism appears in various forms, which makes its detection challenging. Although automated tools can enhance the identification of sexist content, they are often restricted to binary classification. Consequently, more subtle manifestations of sexism may remain undetected due to the lack of fine-grained, context-sensitive labels. To address this issue, we make the following contributions: (1) we present FineMuSe, a new multimodal sexism detection dataset in Spanish that includes both binary and fine-grained annotations; (2) we introduce a comprehensive hierarchical taxonomy that encompasses forms of sexism, non-sexism, and rhetorical devices of irony and humor; and (3) we evaluate a wide range of LLMs for both binary and fine-grained sexism detection. Our findings indicate that multimodal LLMs perform competitively with human annotators in identifying nuanced forms of sexism; however, they struggle to capture co-occurring sexist types when these are conveyed through visual cues.

### 🤖 AI 总结

**一句话总结**：本文提出西班牙语多模态细粒度性别歧视检测数据集FineMuSe及层次化标签体系，并系统评估多模态大模型在识别社交视频中复杂性别歧视表现的能力。

**研究动机**：现有自动化性别歧视检测多停留在二分类层面，难以及时发现以幽默、反语等形式隐含在社交媒体视频中的细微和多类型性别歧视。

**核心方法**：作者构建了包含文本与视觉信息的西班牙语数据集FineMuSe，设计涵盖多种性别歧视类型、非歧视及反讽/幽默的层次化标签体系，并用多种多模态LLM在二分类与细粒度分类任务上进行实验评估。

**主要结论**：实验表明多模态LLM在识别细腻的性别歧视方面已接近人类标注水平，但对于通过视觉线索表达、且同时包含多种性别歧视类型的内容仍存在显著困难。

**关键词**：大语言模型, 多模态LLM, 深度学习, 神经网络, 文本分类, 社会媒体内容审核, 西班牙语语料库, 细粒度情感分析, 层次化标签体系

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15757v1) | [下载PDF](https://arxiv.org/pdf/2602.15757v1.pdf)

---

## [8. Under-resourced studies of under-resourced languages: lemmatization and POS-tagging with LLM annotators for historical Armenian, Georgian, Greek and Syriac](https://arxiv.org/abs/2602.15753v1)

**作者**：Chahan Vidal-Gorène, Bastien Kindt, Florian Cafiero  
**分类**：cs.CL  
**发布时间**：2026-02-17

### 📄 论文摘要

Low-resource languages pose persistent challenges for Natural Language Processing tasks such as lemmatization and part-of-speech (POS) tagging. This paper investigates the capacity of recent large language models (LLMs), including GPT-4 variants and open-weight Mistral models, to address these tasks in few-shot and zero-shot settings for four historically and linguistically diverse under-resourced languages: Ancient Greek, Classical Armenian, Old Georgian, and Syriac. Using a novel benchmark comprising aligned training and out-of-domain test corpora, we evaluate the performance of foundation models across lemmatization and POS-tagging, and compare them with PIE, a task-specific RNN baseline. Our results demonstrate that LLMs, even without fine-tuning, achieve competitive or superior performance in POS-tagging and lemmatization across most languages in few-shot settings. Significant challenges persist for languages characterized by complex morphology and non-Latin scripts, but we demonstrate that LLMs are a credible and relevant option for initiating linguistic annotation tasks in the absence of data, serving as an effective aid for annotation.

### 🤖 AI 总结

**一句话总结**：本文评估GPT-4和Mistral等LLM在零样本/小样本条件下为古希腊语、古亚美尼亚语、古格鲁吉亚语和叙利亚语执行词形还原和词性标注的能力，发现其在多数场景中已能与传统专用模型相媲美甚至更优。

**研究动机**：低资源、尤其是历史语言在词形复杂、标注语料极少的情况下，传统NLP模型难以训练，从而制约了语言学研究和语料标注的开展，因此需要探索无需或仅需极少标注数据即可启动标注工作的技术路径。

**核心方法**：作者构建对齐的训练集与跨领域测试语料作为新基准，针对四种历史语言在词形还原与词性标注任务上，以少样本和零样本提示方式调用多种LLM（GPT-4及开源Mistral），并与专用RNN系统PIE进行系统对比评测。

**主要结论**：实验表明：在少样本设置下，未微调的LLM在大多数语言和任务上已能达到或超过PIE等传统基线，但在形态极其复杂或非拉丁文字体系上仍存在显著困难；总体来看，LLM是缺乏训练数据时启动语言标注工作的可信选项，可作为高效的标注辅助工具。

**关键词**：大语言模型, GPT-4, 机器学习, 少样本学习, 零样本学习, 词形还原, 词性标注, 低资源语言, NLP任务评估, 历史语言处理

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15753v1) | [下载PDF](https://arxiv.org/pdf/2602.15753v1.pdf)

---

## [9. Causal Effect Estimation with Latent Textual Treatments](https://arxiv.org/abs/2602.15730v1)

**作者**：Omri Feldman, Amar Venugopal, Jann Spiess 等 4 位作者  
**分类**：cs.CL, econ.EM  
**发布时间**：2026-02-17

### 📄 论文摘要

Understanding the causal effects of text on downstream outcomes is a central task in many applications. Estimating such effects requires researchers to run controlled experiments that systematically vary textual features. While large language models (LLMs) hold promise for generating text, producing and evaluating controlled variation requires more careful attention. In this paper, we present an end-to-end pipeline for the generation and causal estimation of latent textual interventions. Our work first performs hypothesis generation and steering via sparse autoencoders (SAEs), followed by robust causal estimation. Our pipeline addresses both computational and statistical challenges in text-as-treatment experiments. We demonstrate that naive estimation of causal effects suffers from significant bias as text inherently conflates treatment and covariate information. We describe the estimation bias induced in this setting and propose a solution based on covariate residualization. Our empirical results show that our pipeline effectively induces variation in target features and mitigates estimation error, providing a robust foundation for causal effect estimation in text-as-treatment settings.

### 🤖 AI 总结

**一句话总结**：论文提出一个端到端流程，用稀疏自编码器和因果估计方法在文本作为“潜在处理变量”的场景下估计文本特征对结果的因果效应。

**研究动机**：在很多应用中需要回答“改变文本某个潜在特征会如何影响下游结果”，但文本同时包含处理与协变量信息，直接用LLM生成和估效果估计会产生严重偏差。

**核心方法**：先利用稀疏自编码器在文本表示中发现并操纵可解释的潜在维度以生成受控文本干预，再通过协变量残差化等方法消除文本中协变量信息带来的混淆，从而进行稳健的因果效应估计。

**主要结论**：实验表明，朴素估计在文本处理场景中存在显著偏差，而所提出的基于SAE的干预生成与协变量残差化的因果估计流程能有效操控目标文本特征并显著降低估计误差，为“文本即处理”的因果分析提供了可靠框架。

**关键词**：大语言模型, 因果推断, 文本干预, 稀疏自编码器SAE, 协变量残差化, 文本表示学习, 下游效果估计, llm

**评分**：36

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15730v1) | [下载PDF](https://arxiv.org/pdf/2602.15730v1.pdf)

---

## [10. Rethinking Metrics for Lexical Semantic Change Detection](https://arxiv.org/abs/2602.15716v1)

**作者**：Roksana Goworek, Haim Dubossarsky  
**分类**：cs.CL  
**发布时间**：2026-02-17

### 📄 论文摘要

Lexical semantic change detection (LSCD) increasingly relies on contextualised language model embeddings, yet most approaches still quantify change using a small set of semantic change metrics, primarily Average Pairwise Distance (APD) and cosine distance over word prototypes (PRT). We introduce Average Minimum Distance (AMD) and Symmetric Average Minimum Distance (SAMD), new measures that quantify semantic change via local correspondence between word usages across time periods. Across multiple languages, encoder models, and representation spaces, we show that AMD often provides more robust performance, particularly under dimensionality reduction and with non-specialised encoders, while SAMD excels with specialised encoders. We suggest that LSCD may benefit from considering alternative semantic change metrics beyond APD and PRT, with AMD offering a robust option for contextualised embedding-based analysis.

### 🤖 AI 总结

**一句话总结**：本文提出两种新的词汇语义变化度量AMD和SAMD，相比常用的APD和PRT在多种设置下更稳健、更有效。

**研究动机**：现有基于上下文嵌入的词汇语义变化检测中，度量方式几乎被APD和PRT垄断，缺乏对其他更适合上下文表示的度量指标的系统性探索。

**核心方法**：作者基于跨时间片词用法局部对应关系，提出平均最小距离（AMD）和对称平均最小距离（SAMD）两种新度量，并在多语言、多编码器和不同表示空间下系统对比它们与APD/PRT的表现。

**主要结论**：实验表明AMD在降维或使用非专门语义变化编码器时表现更稳健，而SAMD在专门设计的语义变化编码器下表现最佳，因此LSCD应超越APD和PRT，优先考虑AMD等更适配上下文嵌入的度量方法。

**关键词**：深度学习, 神经网络, embedding, 语义检索, 上下文表示, 时间序列语义演化, 词义变化检测, 平均最小距离, 语义相似度度量

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15716v1) | [下载PDF](https://arxiv.org/pdf/2602.15716v1.pdf)

---

## [11. A Content-Based Framework for Cybersecurity Refusal Decisions in Large Language Models](https://arxiv.org/abs/2602.15689v1)

**作者**：Meirav Segal, Noa Linder, Omer Antverg 等 8 位作者  
**分类**：cs.CL, cs.AI, cs.CR  
**发布时间**：2026-02-17

### 📄 论文摘要

Large language models and LLM-based agents are increasingly used for cybersecurity tasks that are inherently dual-use. Existing approaches to refusal, spanning academic policy frameworks and commercially deployed systems, often rely on broad topic-based bans or offensive-focused taxonomies. As a result, they can yield inconsistent decisions, over-restrict legitimate defenders, and behave brittlely under obfuscation or request segmentation. We argue that effective refusal requires explicitly modeling the trade-off between offensive risk and defensive benefit, rather than relying solely on intent or offensive classification. In this paper, we introduce a content-based framework for designing and auditing cyber refusal policies that makes offense-defense tradeoffs explicit. The framework characterizes requests along five dimensions: Offensive Action Contribution, Offensive Risk, Technical Complexity, Defensive Benefit, and Expected Frequency for Legitimate Users, grounded in the technical substance of the request rather than stated intent. We demonstrate that this content-grounded approach resolves inconsistencies in current frontier model behavior and allows organizations to construct tunable, risk-aware refusal policies.

### 🤖 AI 总结

**一句话总结**：本文提出一个基于内容的五维度框架，用于权衡网络安全场景中LLM回答请求时的进攻风险与防御收益，从而设计更一致且可调的拒答策略。

**研究动机**：现有LLM安全策略多依赖话题黑名单或进攻类目，导致对合法防御者过度限制、在混淆与拆分请求场景下表现脆弱且决策不一致，因此需要一个显式建模攻防权衡的系统方法。

**核心方法**：作者提出以请求“技术实质”为中心的五维度刻画框架：进攻行动贡献、进攻风险、技术复杂度、防御收益、合法用户期望频率，并用该框架分析和审计前沿模型在网络安全请求上的拒答行为，展示如何据此构建可调的风险感知策略。

**主要结论**：内容驱动的多维度刻画相比单纯基于意图或进攻分类更能解释与修正当前模型的不一致拒答行为，能帮助组织制定透明、可审计且可调节的网络安全拒答策略，在保护安全的同时更好支持合法防御用途。

**关键词**：大语言模型, LLM, agent, 多智能体, 安全策略评估, 网络安全辅助决策, 内容审查框架, 攻防权衡建模, 拒答策略优化

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15689v1) | [下载PDF](https://arxiv.org/pdf/2602.15689v1.pdf)

---

## cs.CV

## [12. VideoSketcher: Video Models Prior Enable Versatile Sequential Sketch Generation](https://arxiv.org/abs/2602.15819v1)

**作者**：Hui Ren, Yuval Alaluf, Omer Bar Tal 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-17

### 📄 论文摘要

Sketching is inherently a sequential process, in which strokes are drawn in a meaningful order to explore and refine ideas. However, most generative models treat sketches as static images, overlooking the temporal structure that underlies creative drawing. We present a data-efficient approach for sequential sketch generation that adapts pretrained text-to-video diffusion models to generate sketching processes. Our key insight is that large language models and video diffusion models offer complementary strengths for this task: LLMs provide semantic planning and stroke ordering, while video diffusion models serve as strong renderers that produce high-quality, temporally coherent visuals. We leverage this by representing sketches as short videos in which strokes are progressively drawn on a blank canvas, guided by text-specified ordering instructions. We introduce a two-stage fine-tuning strategy that decouples the learning of stroke ordering from the learning of sketch appearance. Stroke ordering is learned using synthetic shape compositions with controlled temporal structure, while visual appearance is distilled from as few as seven manually authored sketching processes that capture both global drawing order and the continuous formation of individual strokes. Despite the extremely limited amount of human-drawn sketch data, our method generates high-quality sequential sketches that closely follow text-specified orderings while exhibiting rich visual detail. We further demonstrate the flexibility of our approach through extensions such as brush style conditioning and autoregressive sketch generation, enabling additional controllability and interactive, collaborative drawing.

### 🤖 AI 总结

**一句话总结**：VideoSketcher 将预训练文本到视频扩散模型与大模型规划能力结合，用极少人类数据生成按指定笔画顺序演化的高质量素描视频。

**研究动机**：现有素描生成多视素描为静态图像，忽略实际绘画中“按顺序逐步落笔”的时间结构，难以表达创作过程和交互性控制。

**核心方法**：将素描表示为“从空白画布逐步加笔画”的短视频，利用LLM生成语义与笔画顺序指令，以视频扩散模型作为通用渲染器，并采用两阶段微调：先在合成几何形状上学习时间顺序结构，再用少量真实素描过程蒸馏视觉外观与连续笔画形成；同时扩展画笔风格条件与自回归生成以支持交互绘制。

**主要结论**：在仅依赖极少人工绘画数据的情况下，该方法能生成既遵循文本指定绘制顺序又具丰富细节的连续素描过程，并可通过风格控制与自回归扩展实现更灵活、互动性更强的绘画应用。

**关键词**：扩散模型, 大型语言模型, 视频生成, 文本到视频, 顺序草图生成, 笔画顺序建模, 自回归生成, 条件生成, 交互式绘画, 协同创作, llm

**评分**：43

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15819v1) | [下载PDF](https://arxiv.org/pdf/2602.15819v1.pdf)

---

## [13. Task-Agnostic Continual Learning for Chest Radiograph Classification](https://arxiv.org/abs/2602.15811v1)

**作者**：Muthu Subash Kavitha, Anas Zafar, Amgad Muneer 等 4 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-02-17

### 📄 论文摘要

Clinical deployment of chest radiograph classifiers requires models that can be updated as new datasets become available without retraining on previously ob- served data or degrading validated performance. We study, for the first time, a task-incremental continual learning setting for chest radiograph classification, in which heterogeneous chest X-ray datasets arrive sequentially and task identifiers are unavailable at inference. We propose a continual adapter-based routing learning strategy for Chest X-rays (CARL-XRay) that maintains a fixed high-capacity backbone and incrementally allocates lightweight task-specific adapters and classifier heads. A latent task selector operates on task-adapted features and leverages both current and historical context preserved through compact prototypes and feature-level experience replay. This design supports stable task identification and adaptation across sequential updates while avoiding raw-image storage. Experiments on large-scale public chest radiograph datasets demonstrate robust performance retention and reliable task-aware inference under continual dataset ingestion. CARL-XRay outperforms joint training under task-unknown deployment, achieving higher routing accuracy (75.0\% vs.\ 62.5\%), while maintaining competitive diagnostic performance with AUROC of 0.74 in the oracle setting with ground-truth task identity and 0.75 under task-unknown inference, using significantly fewer trainable parameters. Finally, the proposed framework provides a practical alternative to joint training and repeated full retraining in continual clinical deployment.

### 🤖 AI 总结

**一句话总结**：论文提出CARL-XRay框架，在无需保存历史影像与任务标签的前提下，实现胸片分类的任务无关持续学习，并在路由准确率和诊断性能上优于联合训练。

**研究动机**：临床部署中的胸片分类模型需要在新数据集持续到来时更新模型，同时避免遗忘已验证性能且无法重新访问历史数据与依赖显式任务标识。

**核心方法**：CARL-XRay采用固定高容量主干网络，针对每个新数据集增量加入轻量适配器和分类头，并通过原型和特征级经验回放构建潜在任务选择器，实现在不存储原始影像的情况下进行任务识别与路由。

**主要结论**：在多个大规模胸片数据集的持续学习实验中，CARL-XRay在任务未知部署场景下获得更高的路由准确率（75.0% vs 62.5%），在诊断AUROC上与oracle设定相当且参数量更少，为临床持续部署提供了优于反复全量重训的实用替代方案。

**关键词**：深度学习, 神经网络, 持续学习, 任务增量学习, 适配器网络, 乳腺X光分类, 特征重放, 原型表示, 表示学习, 医学影像分析, rag

**评分**：33

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15811v1) | [下载PDF](https://arxiv.org/pdf/2602.15811v1.pdf)

---

## [14. Context-aware Skin Cancer Epithelial Cell Classification with Scalable Graph Transformers](https://arxiv.org/abs/2602.15783v1)

**作者**：Lucas Sancéré, Noémie Moreau, Katarzyna Bozek  
**分类**：cs.CV  
**发布时间**：2026-02-17

### 📄 论文摘要

Whole-slide images (WSIs) from cancer patients contain rich information that can be used for medical diagnosis or to follow treatment progress. To automate their analysis, numerous deep learning methods based on convolutional neural networks and Vision Transformers have been developed and have achieved strong performance in segmentation and classification tasks. However, due to the large size and complex cellular organization of WSIs, these models rely on patch-based representations, losing vital tissue-level context. We propose using scalable Graph Transformers on a full-WSI cell graph for classification. We evaluate this methodology on a challenging task: the classification of healthy versus tumor epithelial cells in cutaneous squamous cell carcinoma (cSCC), where both cell types exhibit very similar morphologies and are therefore difficult to differentiate for image-based approaches. We first compared image-based and graph-based methods on a single WSI. Graph Transformer models SGFormer and DIFFormer achieved balanced accuracies of $85.2 \pm 1.5$ ($\pm$ standard error) and $85.1 \pm 2.5$ in 3-fold cross-validation, respectively, whereas the best image-based method reached $81.2 \pm 3.0$. By evaluating several node feature configurations, we found that the most informative representation combined morphological and texture features as well as the cell classes of non-epithelial cells, highlighting the importance of the surrounding cellular context. We then extended our work to train on several WSIs from several patients. To address the computational constraints of image-based models, we extracted four $2560 \times 2560$ pixel patches from each image and converted them into graphs. In this setting, DIFFormer achieved a balanced accuracy of $83.6 \pm 1.9$ (3-fold cross-validation), while the state-of-the-art image-based model CellViT256 reached $78.1 \pm 0.5$.

### 🤖 AI 总结

**一句话总结**：本文利用可扩展图Transformer在全切片细胞图上进行上下文感知的皮肤鳞状细胞癌上皮细胞良恶性分类，相比图像补丁方法显著提升分类精度。

**研究动机**：传统CNN和ViT在超大病理全切片图像上依赖补丁表示，难以利用组织级空间关系，且在形态极其相似的良性/肿瘤上皮细胞区分任务上性能受限。

**核心方法**：作者将WSI细胞检测结果构建为细胞级图，节点包含形态特征、纹理特征及周围非上皮细胞类别信息，并采用可扩展的Graph Transformer（SGFormer、DIFFormer）在单张及多张WSI上进行节点分类；多WSI场景中将每张WSI划分为多个大补丁后再转为子图以缓解计算压力。

**主要结论**：在单WSI和多WSI设置下，Graph Transformer（尤其是DIFFormer）均在balanced accuracy上显著优于最优图像方法（如CellViT256），且实验表明结合细胞形态、纹理与邻域细胞类别的上下文信息对上皮细胞良恶性判别至关重要，证明全切片细胞图+图Transformer是复杂组织病理分类的有效途径。

**关键词**：深度学习, 图神经网络, GraphTransformer, 皮肤癌病理图像, 细胞级分类, 上下文感知建模, 可扩展图表示, 医学影像分析

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15783v1) | [下载PDF](https://arxiv.org/pdf/2602.15783v1.pdf)

---

## [15. Meteorological data and Sky Images meets Neural Models for Photovoltaic Power Forecasting](https://arxiv.org/abs/2602.15782v1)

**作者**：Ines Montoya-Espinagosa, Antonio Agudo  
**分类**：cs.CV  
**发布时间**：2026-02-17

### 📄 论文摘要

Due to the rise in the use of renewable energies as an alternative to traditional ones, and especially solar energy, there is increasing interest in studying how to address photovoltaic forecasting in the face of the challenge of variability in photovoltaic energy production, using different methodologies. This work develops a hybrid approach for short and long-term forecasting based on two studies with the same purpose. A multimodal approach that combines images of the sky and photovoltaic energy history with meteorological data is proposed. The main goal is to improve the accuracy of ramp event prediction, increase the robustness of forecasts in cloudy conditions, and extend capabilities beyond nowcasting, to support more efficient operation of the power grid and better management of solar variability. Deep neural models are used for both nowcasting and forecasting solutions, incorporating individual and multiple meteorological variables, as well as an analytical solar position. The results demonstrate that the inclusion of meteorological data, particularly the surface long-wave, radiation downwards, and the combination of wind and solar position, significantly improves current predictions in both nowcasting and forecasting tasks, especially on cloudy days. This study highlights the importance of integrating diverse data sources to improve the reliability and interpretability of solar energy prediction models.

### 🤖 AI 总结

**一句话总结**：本文提出利用天空图像、光伏历史功率和气象数据的多模态深度学习模型，实现短期与长期光伏功率预测性能的显著提升，尤其在多云与剧烈爬坡工况下效果更佳。

**研究动机**：光伏出力受云层等因素影响波动大，给电网调度和可再生能源消纳带来挑战，因此需要更准确、对云天等复杂天气更鲁棒的短中期光伏功率预测方法。

**核心方法**：构建以深度神经网络为核心的混合多模态框架，将天空图像、光伏功率时间序列、多个气象变量及解析太阳位置联合输入，用于同时解决超短期nowcasting和更长时段forecasting任务，并系统对比不同气象变量组合对预测效果的贡献。

**主要结论**：引入气象特征，特别是下行长波辐射、风场与太阳位置等信息，可显著提升晴天与多云条件下的光伏功率预测精度和爬坡事件捕捉能力，证明多源数据融合与可解释气象变量对提升光伏预测可靠性具有关键作用。

**关键词**：深度学习, 神经网络, 多模态预测, 光伏功率预测, 气象数据融合, 天空图像分析, 短期与长期预测, 云天条件鲁棒性, agent

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15782v1) | [下载PDF](https://arxiv.org/pdf/2602.15782v1.pdf)

---

## [16. NeRFscopy: Neural Radiance Fields for in-vivo Time-Varying Tissues from Endoscopy](https://arxiv.org/abs/2602.15775v1)

**作者**：Laura Salort-Benejam, Antonio Agudo  
**分类**：cs.CV  
**发布时间**：2026-02-17

### 📄 论文摘要

Endoscopy is essential in medical imaging, used for diagnosis, prognosis and treatment. Developing a robust dynamic 3D reconstruction pipeline for endoscopic videos could enhance visualization, improve diagnostic accuracy, aid in treatment planning, and guide surgery procedures. However, challenges arise due to the deformable nature of the tissues, the use of monocular cameras, illumination changes, occlusions and unknown camera trajectories. Inspired by neural rendering, we introduce NeRFscopy, a self-supervised pipeline for novel view synthesis and 3D reconstruction of deformable endoscopic tissues from a monocular video. NeRFscopy includes a deformable model with a canonical radiance field and a time-dependent deformation field parameterized by SE(3) transformations. In addition, the color images are efficiently exploited by introducing sophisticated terms to learn a 3D implicit model without assuming any template or pre-trained model, solely from data. NeRFscopy achieves accurate results in terms of novel view synthesis, outperforming competing methods across various challenging endoscopy scenes.

### 🤖 AI 总结

**一句话总结**：NeRFscopy提出一种面向单目内窥镜视频的自监督NeRF框架，实现可变形活体组织的动态3D重建与新视角合成。

**研究动机**：内窥镜成像中组织高度可变形、相机单目且轨迹未知、光照变化大，使得现有3D重建和新视图合成方法难以在临床场景中稳定工作，需要专门的动态重建方法提升诊断和术中导航能力。

**核心方法**：方法构建一个包含规范辐射场与随时间变化的变形场的NeRF模型，通过SE(3)参数化的时变形变形场将各帧对齐到规范空间，并设计利用彩色图像的自监督损失项，在无需模板或预训练模型的条件下从单目视频学习隐式3D表示。

**主要结论**：在多种复杂内窥镜场景上，NeRFscopy在新视角合成精度上优于现有方法，并能生成高质量的动态3D组织重建，验证了该自监督变形NeRF框架在活体内窥镜应用中的有效性。

**关键词**：深度学习, 神经网络, NeRF, 神经辐射场, 自监督学习, 三维重建, 内镜医学影像, 动态组织建模, 视角合成, agent

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15775v1) | [下载PDF](https://arxiv.org/pdf/2602.15775v1.pdf)

---

## [17. Understanding vs. Generation: Navigating Optimization Dilemma in Multimodal Models](https://arxiv.org/abs/2602.15772v1)

**作者**：Sen Ye, Mengde Xu, Shuyang Gu 等 6 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-02-17

### 📄 论文摘要

Current research in multimodal models faces a key challenge where enhancing generative capabilities often comes at the expense of understanding, and vice versa. We analyzed this trade-off and identify the primary cause might be the potential conflict between generation and understanding, which creates a competitive dynamic within the model. To address this, we propose the Reason-Reflect-Refine (R3) framework. This innovative algorithm re-frames the single-step generation task into a multi-step process of "generate-understand-regenerate". By explicitly leveraging the model's understanding capability during generation, we successfully mitigate the optimization dilemma, achieved stronger generation results and improved understanding ability which are related to the generation process. This offers valuable insights for designing next-generation unified multimodal models. Code is available at https://github.com/sen-ye/R3.

### 🤖 AI 总结

**一句话总结**：论文提出Reason-Reflect-Refine（R3）多步生成框架，在多模态模型中同时提升生成与理解能力，缓解二者之间的优化冲突。

**研究动机**：现有多模态模型在优化生成能力时往往牺牲理解能力，反之亦然，说明生成和理解存在竞争与冲突，亟需一种能够协调两者的训练与推理机制。

**核心方法**：R3框架将原本单步的“直接生成”重构为“推理生成（Reason）—理解反思（Reflect）—再生成精炼（Refine）”三步流程，在生成过程中显式调用模型的理解能力，从而联合优化理解与生成。

**主要结论**：通过R3框架，多模态模型在生成质量和与生成相关的理解任务上都取得提升，证明利用多步“生成-理解-再生成”流程可以有效缓解生成与理解之间的优化两难，并为下一代统一多模态模型设计提供思路。

**关键词**：深度学习, 多模态模型, 生成式模型, 理解能力, Reason-Reflect-Refine, R3框架, 推理优化, 多步骤生成, 对比实验, 模型训练策略, generative

**评分**：20

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15772v1) | [下载PDF](https://arxiv.org/pdf/2602.15772v1.pdf)

---

## [18. RaCo: Ranking and Covariance for Practical Learned Keypoints](https://arxiv.org/abs/2602.15755v1)

**作者**：Abhiram Shenoi, Philipp Lindenberger, Paul-Edouard Sarlin 等 4 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-02-17

### 📄 论文摘要

This paper introduces RaCo, a lightweight neural network designed to learn robust and versatile keypoints suitable for a variety of 3D computer vision tasks. The model integrates three key components: the repeatable keypoint detector, a differentiable ranker to maximize matches with a limited number of keypoints, and a covariance estimator to quantify spatial uncertainty in metric scale. Trained on perspective image crops only, RaCo operates without the need for covisible image pairs. It achieves strong rotational robustness through extensive data augmentation, even without the use of computationally expensive equivariant network architectures. The method is evaluated on several challenging datasets, where it demonstrates state-of-the-art performance in keypoint repeatability and two-view matching, particularly under large in-plane rotations. Ultimately, RaCo provides an effective and simple strategy to independently estimate keypoint ranking and metric covariance without additional labels, detecting interpretable and repeatable interest points. The code is available at https://github.com/cvg/RaCo.

### 🤖 AI 总结

**一句话总结**：RaCo 提出一种轻量级神经网络，同时学习关键点的可重复检测、排序与度量尺度协方差，在多种3D视觉任务和大角度旋转场景下取得SOTA性能。

**研究动机**：传统关键点方法难以在多任务、多视角尤其是大旋转条件下兼顾可重复性、匹配效率和不确定性估计，并且往往需要协视图训练或昂贵的等变结构。

**核心方法**：RaCo 包含三部分：可重复关键点检测器、可微排序模块在给定数量约束下最大化匹配数，以及协方差估计器输出空间不确定性；通过仅使用透视图裁剪和强旋转增强进行训练，无需协可见图像对或额外标签。

**主要结论**：实验表明，RaCo 在多个数据集上实现了在关键点可重复性和双视图匹配上的先进性能，尤其在大平面内旋转下表现突出，并以简单高效的框架实现关键点排名与度量协方差的独立估计，检测到可解释且稳定的兴趣点。

**关键词**：深度学习, 神经网络, 特征点检测, 可微排序, 协方差估计, 三维计算机视觉, 两视图匹配, 旋转鲁棒性, RaCo模型, neural network

**评分**：22

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15755v1) | [下载PDF](https://arxiv.org/pdf/2602.15755v1.pdf)

---

## [19. Language and Geometry Grounded Sparse Voxel Representations for Holistic Scene Understanding](https://arxiv.org/abs/2602.15734v1)

**作者**：Guile Wu, David Huang, Bingbing Liu 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-17

### 📄 论文摘要

Existing 3D open-vocabulary scene understanding methods mostly emphasize distilling language features from 2D foundation models into 3D feature fields, but largely overlook the synergy among scene appearance, semantics, and geometry. As a result, scene understanding often deviates from the underlying geometric structure of scenes and becomes decoupled from the reconstruction process. In this work, we propose a novel approach that leverages language and geometry grounded sparse voxel representations to comprehensively model appearance, semantics, and geometry within a unified framework. Specifically, we use 3D sparse voxels as primitives and employ an appearance field, a density field, a feature field, and a confidence field to holistically represent a 3D scene. To promote synergy among the appearance, density, and feature fields, we construct a feature modulation module and distill language features from a 2D foundation model into our 3D scene model. In addition, we integrate geometric distillation into feature field distillation to transfer geometric knowledge from a geometry foundation model to our 3D scene representations via depth correlation regularization and pattern consistency regularization. These components work together to synergistically model the appearance, semantics, and geometry of the 3D scene within a unified framework. Extensive experiments demonstrate that our approach achieves superior overall performance compared with state-of-the-art methods in holistic scene understanding and reconstruction.

### 🤖 AI 总结

**一句话总结**：提出一种同时利用语言与几何信息的稀疏体素3D表示，在统一框架下实现对场景外观、语义和几何的整体建模，从而提升开放词汇场景理解与重建性能。

**研究动机**：现有3D开放词汇场景理解方法主要从2D视觉-语言模型蒸馏语义特征，忽视外观、语义与几何之间的协同，导致语义结果与几何结构脱节、与重建过程割裂。

**核心方法**：以3D稀疏体素为基本单元，构建外观场、密度场、特征场和置信度场四种场；通过特征调制模块将外观、密度与语义特征深度耦合，并从2D视觉-语言基础模型蒸馏语言特征，同时引入几何基础模型的几何蒸馏，用深度相关约束与模式一致性约束将几何知识注入3D特征场。

**主要结论**：在多个场景理解与重建任务和数据集上，该方法在整体性能上优于现有最新方法，表明语言与几何双重蒸馏的稀疏体素统一表示能够更好地兼顾开放词汇语义理解与高质量3D重建。

**关键词**：深度学习, 神经网络, 多模态表征, 3D场景理解, 稀疏体素表示, 语言引导特征蒸馏, 几何感知重建, open-vocabulary识别, rag

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15734v1) | [下载PDF](https://arxiv.org/pdf/2602.15734v1.pdf)

---

## [20. Spanning the Visual Analogy Space with a Weight Basis of LoRAs](https://arxiv.org/abs/2602.15727v1)

**作者**：Hila Manor, Rinon Gal, Haggai Maron 等 5 位作者  
**分类**：cs.CV, cs.AI, cs.GR, cs.LG, eess.IV  
**发布时间**：2026-02-17

### 📄 论文摘要

Visual analogy learning enables image manipulation through demonstration rather than textual description, allowing users to specify complex transformations difficult to articulate in words. Given a triplet $\{\mathbf{a}$, $\mathbf{a}'$, $\mathbf{b}\}$, the goal is to generate $\mathbf{b}'$ such that $\mathbf{a} : \mathbf{a}' :: \mathbf{b} : \mathbf{b}'$. Recent methods adapt text-to-image models to this task using a single Low-Rank Adaptation (LoRA) module, but they face a fundamental limitation: attempting to capture the diverse space of visual transformations within a fixed adaptation module constrains generalization capabilities. Inspired by recent work showing that LoRAs in constrained domains span meaningful, interpolatable semantic spaces, we propose LoRWeB, a novel approach that specializes the model for each analogy task at inference time through dynamic composition of learned transformation primitives, informally, choosing a point in a "space of LoRAs". We introduce two key components: (1) a learnable basis of LoRA modules, to span the space of different visual transformations, and (2) a lightweight encoder that dynamically selects and weighs these basis LoRAs based on the input analogy pair. Comprehensive evaluations demonstrate our approach achieves state-of-the-art performance and significantly improves generalization to unseen visual transformations. Our findings suggest that LoRA basis decompositions are a promising direction for flexible visual manipulation. Code and data are in https://research.nvidia.com/labs/par/lorweb

### 🤖 AI 总结

**一句话总结**：LoRWeB 通过构建一组可组合的 LoRA 基向量，并在推理时按类比输入动态加权组合，实现更泛化的视觉类比编辑。

**研究动机**：单一 LoRA 适配无法覆盖多样且复杂的视觉变换空间，导致视觉类比任务在泛化到未见过的变换时表现受限。

**核心方法**：首先预训练一组表示不同视觉变换“原语”的 LoRA 基模块，然后用轻量编码器根据给定类比对 {a, a'} 学习权重，在推理时对这些 LoRA 基进行加权组合，得到特定任务的专用 LoRA 来生成 b'。

**主要结论**：基于 LoRA 基分解与动态组合的 LoRWeB 在视觉类比基准上达到 SOTA，并在未见类变换上的泛化显著提升，表明以“LoRA 空间”方式建模变换是灵活视觉操作的有效方向。

**关键词**：深度学习, 生成式模型, LoRA权重基分解, 视觉类比学习, 图像编辑, 文本到图像扩散模型, 动态模块组合, 视觉变换泛化, agent

**评分**：39

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15727v1) | [下载PDF](https://arxiv.org/pdf/2602.15727v1.pdf)

---

## [21. Learning to Retrieve Navigable Candidates for Efficient Vision-and-Language Navigation](https://arxiv.org/abs/2602.15724v1)

**作者**：Shutian Gu, Chengkai Huang, Ruoyu Wang 等 4 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-02-17

### 📄 论文摘要

Vision-and-Language Navigation (VLN) requires an agent to follow natural-language instructions and navigate through previously unseen environments. Recent approaches increasingly employ large language models (LLMs) as high-level navigators due to their flexibility and reasoning capability. However, prompt-based LLM navigation often suffers from inefficient decision-making, as the model must repeatedly interpret instructions from scratch and reason over noisy and verbose navigable candidates at each step. In this paper, we propose a retrieval-augmented framework to improve the efficiency and stability of LLM-based VLN without modifying or fine-tuning the underlying language model. Our approach introduces retrieval at two complementary levels. At the episode level, an instruction-level embedding retriever selects semantically similar successful navigation trajectories as in-context exemplars, providing task-specific priors for instruction grounding. At the step level, an imitation-learned candidate retriever prunes irrelevant navigable directions before LLM inference, reducing action ambiguity and prompt complexity. Both retrieval modules are lightweight, modular, and trained independently of the LLM. We evaluate our method on the Room-to-Room (R2R) benchmark. Experimental results demonstrate consistent improvements in Success Rate, Oracle Success Rate, and SPL on both seen and unseen environments. Ablation studies further show that instruction-level exemplar retrieval and candidate pruning contribute complementary benefits to global guidance and step-wise decision efficiency. These results indicate that retrieval-augmented decision support is an effective and scalable strategy for enhancing LLM-based vision-and-language navigation.

### 🤖 AI 总结

**一句话总结**：本文提出一个检索增强框架，在不微调LLM的前提下，通过轨迹示例检索与候选动作检索提升视觉-语言导航的效率与稳定性。

**研究动机**：现有基于LLM的VLN方法在每一步都需重新理解指令并在大量噪声候选动作间推理，导致决策效率低且不稳定。

**核心方法**：方法在两个层面引入检索：1）episode层用指令嵌入检索语义相似且成功的导航轨迹作为in-context示例；2）step层用模仿学习训练的候选检索器预先剪枝无关可行方向，从而简化LLM输入与决策空间，两模块均独立于LLM训练。

**主要结论**：在R2R基准上，该方法在已见和未见环境的成功率、Oracle成功率和SPL上均有提升，消融实验证明轨迹示例检索与候选剪枝在全局引导和逐步决策效率上具有互补收益，表明检索增强决策是提升LLM导航能力的有效且可扩展策略。

**关键词**：大语言模型, 检索增强, RAG, 指令级嵌入, 候选动作检索, 视觉导航, 模仿学习, 室内三维环境

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15724v1) | [下载PDF](https://arxiv.org/pdf/2602.15724v1.pdf)

---

## cs.LG

## [22. Operationalising the Superficial Alignment Hypothesis via Task Complexity](https://arxiv.org/abs/2602.15829v1)

**作者**：Tomás Vergara-Browne, Darshan Patil, Ivan Titov 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-17

### 📄 论文摘要

The superficial alignment hypothesis (SAH) posits that large language models learn most of their knowledge during pre-training, and that post-training merely surfaces this knowledge. The SAH, however, lacks a precise definition, which has led to (i) different and seemingly orthogonal arguments supporting it, and (ii) important critiques to it. We propose a new metric called task complexity: the length of the shortest program that achieves a target performance on a task. In this framework, the SAH simply claims that pre-trained models drastically reduce the complexity of achieving high performance on many tasks. Our definition unifies prior arguments supporting the SAH, interpreting them as different strategies to find such short programs. Experimentally, we estimate the task complexity of mathematical reasoning, machine translation, and instruction following; we then show that these complexities can be remarkably low when conditioned on a pre-trained model. Further, we find that pre-training enables access to strong performances on our tasks, but it can require programs of gigabytes of length to access them. Post-training, on the other hand, collapses the complexity of reaching this same performance by several orders of magnitude. Overall, our results highlight that task adaptation often requires surprisingly little information -- often just a few kilobytes.

### 🤖 AI 总结

**一句话总结**：论文用“任务复杂度”这一可形式化的指标来刻画表层对齐假说：预训练大模型已蕴含能力，而微调只是找到访问这些能力的极短“程序”。

**研究动机**：现有表层对齐假说缺乏精确定义，导致支持与反对观点分散、难以比较，作者希望用一个统一的理论框架来量化“预训练学到什么、微调又做了多少事”。

**核心方法**：引入任务复杂度为“达到某一性能所需的最短程序长度”，并在给定预训练模型作为条件的前提下，用不同形式的“程序”（如微调参数、指令格式等）估计数学推理、机器翻译和指令跟随等任务的复杂度。

**主要结论**：实验表明，相对于从零开始，给定预训练模型后要获得高性能所需的信息量（程序长度）可以极小（往往仅需KB级），而预训练虽蕴含强能力但若无后续适配则等效“程序”可达GB级，微调则显著压缩了访问这些能力的复杂度，从而以统一视角支持表层对齐假说。

**关键词**：大语言模型, 深度学习, 神经网络, 任务复杂度, 指令微调, 数学推理, 机器翻译, 程序搜索, 模型对齐, 少样本学习, agent

**评分**：20

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15829v1) | [下载PDF](https://arxiv.org/pdf/2602.15829v1.pdf)

---

## [23. Stabilizing Test-Time Adaptation of High-Dimensional Simulation Surrogates via D-Optimal Statistics](https://arxiv.org/abs/2602.15820v1)

**作者**：Anna Zimmel, Paul Setinek, Gianluca Galletti 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-17

### 📄 论文摘要

Machine learning surrogates are increasingly used in engineering to accelerate costly simulations, yet distribution shifts between training and deployment often cause severe performance degradation (e.g., unseen geometries or configurations). Test-Time Adaptation (TTA) can mitigate such shifts, but existing methods are largely developed for lower-dimensional classification with structured outputs and visually aligned input-output relationships, making them unstable for the high-dimensional, unstructured and regression problems common in simulation. We address this challenge by proposing a TTA framework based on storing maximally informative (D-optimal) statistics, which jointly enables stable adaptation and principled parameter selection at test time. When applied to pretrained simulation surrogates, our method yields up to 7% out-of-distribution improvements at negligible computational cost. To the best of our knowledge, this is the first systematic demonstration of effective TTA for high-dimensional simulation regression and generative design optimization, validated on the SIMSHIFT and EngiBench benchmarks.

### 🤖 AI 总结

**一句话总结**：提出一种基于D-optimal统计的测试时自适应框架，使高维仿真替代模型在分布偏移下保持稳定并提升OOD性能。

**研究动机**：工程仿真替代模型在部署时常遇到训练分布外的几何和配置，导致性能显著下降，而现有TTA方法主要针对低维分类任务，难以稳定应用于高维回归型仿真场景。

**核心方法**：在预训练阶段存储能最大化信息量的D-optimal统计量，并在测试时利用这些统计指导模型参数的稳定自适应与超参数选择，从而在几乎不增加计算成本的前提下实现鲁棒TTA。

**主要结论**：在SIMSHIFT和EngiBench高维仿真与生成式设计优化基准上，方法实现最高约7%的OOD性能提升，首次系统证明了TTA在高维仿真回归与设计优化场景中的有效性和实用性。

**关键词**：机器学习, 深度学习, 测试时自适应, 高维仿真代理模型, 分布移位鲁棒性, 生成式设计优化, 工程仿真加速, 仿真代理基准数据集, machine learning

**评分**：39

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15820v1) | [下载PDF](https://arxiv.org/pdf/2602.15820v1.pdf)

---

## [24. Solving Parameter-Robust Avoid Problems with Unknown Feasibility using Reinforcement Learning](https://arxiv.org/abs/2602.15817v1)

**作者**：Oswin So, Eric Yang Yu, Songyuan Zhang 等 6 位作者  
**分类**：cs.LG, cs.RO, math.OC  
**发布时间**：2026-02-17

### 📄 论文摘要

Recent advances in deep reinforcement learning (RL) have achieved strong results on high-dimensional control tasks, but applying RL to reachability problems raises a fundamental mismatch: reachability seeks to maximize the set of states from which a system remains safe indefinitely, while RL optimizes expected returns over a user-specified distribution. This mismatch can result in policies that perform poorly on low-probability states that are still within the safe set. A natural alternative is to frame the problem as a robust optimization over a set of initial conditions that specify the initial state, dynamics and safe set, but whether this problem has a solution depends on the feasibility of the specified set, which is unknown a priori. We propose Feasibility-Guided Exploration (FGE), a method that simultaneously identifies a subset of feasible initial conditions under which a safe policy exists, and learns a policy to solve the reachability problem over this set of initial conditions. Empirical results demonstrate that FGE learns policies with over 50% more coverage than the best existing method for challenging initial conditions across tasks in the MuJoCo simulator and the Kinetix simulator with pixel observations.

### 🤖 AI 总结

**一句话总结**：论文提出一种名为 Feasibility-Guided Exploration (FGE) 的强化学习方法，在未知可行性的情况下同时发现可行初始条件集合并学习安全规避策略，从而显著提升可安全控制的状态覆盖率。

**研究动机**：传统深度强化学习优化的是给定分布下的期望回报，而可达性/安全规避问题关注的是“从尽可能多的初始状态起始都能一直保持安全”，两者目标错位且初始条件的可行性事先未知，导致现有方法在低概率但仍属安全集的状态上表现极差。

**核心方法**：FGE 将问题表述为对初始条件（包括初始状态、动力学和安全集）的鲁棒优化，一边通过探索识别出存在安全策略的可行初始条件子集，一边在该子集上训练强化学习策略以最大化安全可达集；核心在于利用可行性信号指导探索，而非仅依赖密集回报或预设分布。

**主要结论**：在 MuJoCo 和 Kinetix（像素观测）等仿真环境中，FGE 相比现有最优方法在困难初始条件上的安全覆盖率提升超过 50%，说明该方法能在未知可行性下更有效地找到并利用可安全控制的状态空间。

**关键词**：深度强化学习, 神经网络, 安全控制, 可行性探索, 鲁棒优化, 覆盖率最大化, 高维控制, 策略学习, MuJoCo环境, Kinetix模拟器, rag

**评分**：20

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15817v1) | [下载PDF](https://arxiv.org/pdf/2602.15817v1.pdf)

---

## [25. The Geometry of Alignment Collapse: When Fine-Tuning Breaks Safety](https://arxiv.org/abs/2602.15799v1)

**作者**：Max Springer, Chung Peng Lee, Blossom Metevier 等 8 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-17

### 📄 论文摘要

Fine-tuning aligned language models on benign tasks unpredictably degrades safety guardrails, even when training data contains no harmful content and developers have no adversarial intent. We show that the prevailing explanation, that fine-tuning updates should be orthogonal to safety-critical directions in high-dimensional parameter space, offers false reassurance: we show this orthogonality is structurally unstable and collapses under the dynamics of gradient descent. We then resolve this through a novel geometric analysis, proving that alignment concentrates in low-dimensional subspaces with sharp curvature, creating a brittle structure that first-order methods cannot detect or defend. While initial fine-tuning updates may indeed avoid these subspaces, the curvature of the fine-tuning loss generates second-order acceleration that systematically steers trajectories into alignment-sensitive regions. We formalize this mechanism through the Alignment Instability Condition, three geometric properties that, when jointly satisfied, lead to safety degradation. Our main result establishes a quartic scaling law: alignment loss grows with the fourth power of training time, governed by the sharpness of alignment geometry and the strength of curvature coupling between the fine-tuning task and safety-critical parameters. These results expose a structural blind spot in the current safety paradigm. The dominant approaches to safe fine-tuning address only the initial snapshot of a fundamentally dynamic problem. Alignment fragility is not a bug to be patched; it is an intrinsic geometric property of gradient descent on curved manifolds. Our results motivate the development of curvature-aware methods, and we hope will further enable a shift in alignment safety analysis from reactive red-teaming to predictive diagnostics for open-weight model deployment.

### 🤖 AI 总结

**一句话总结**：论文从几何视角证明：看似“安全无害”的微调也会在梯度下降动力学下不可预期地破坏对齐与安全防护，这是训练过程在弯曲参数流形上的内在不稳定性，而非简单工程失误。

**研究动机**：实践中发现即使在完全良性的下游任务上微调对齐过的大模型，安全 guardrail 仍会退化，而现有“微调梯度与安全方向近似正交就安全”的直觉解释不了这种现象，因而需要从更基础的几何和动力系统角度重新审视安全微调。

**核心方法**：作者把参数空间视为具有曲率的流形，分析对齐方向集中在低维高曲率子空间的几何结构，推导梯度下降在该流形上的二阶加速度效应，形式化提出“对齐不稳定条件”，并给出训练时间与对齐损失呈四次方增长的标度律。

**主要结论**：对齐信息以极脆弱的低维高曲率结构存在，初始梯度虽可与其近似正交，但随训练推进曲率会系统性地将微调轨迹拐入对齐敏感区，从而导致安全性退化；因此当前仅关注初始梯度/数据分布的安全微调范式存在结构性盲点，需要发展曲率感知、能预测对齐崩塌风险的诊断与训练方法。

**关键词**：对齐, 大型语言模型, 安全微调, 梯度下降, 曲率敏感性, 对齐不稳定性, 安全约束退化, 曲率感知优化, 开放权重模型部署, rag

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15799v1) | [下载PDF](https://arxiv.org/pdf/2602.15799v1.pdf)

---

## [26. GLM-5: from Vibe Coding to Agentic Engineering](https://arxiv.org/abs/2602.15763v1)

**作者**：GLM-5 Team, :, Aohan Zeng 等 187 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-02-17

### 📄 论文摘要

We present GLM-5, a next-generation foundation model designed to transition the paradigm of vibe coding to agentic engineering. Building upon the agentic, reasoning, and coding (ARC) capabilities of its predecessor, GLM-5 adopts DSA to significantly reduce training and inference costs while maintaining long-context fidelity. To advance model alignment and autonomy, we implement a new asynchronous reinforcement learning infrastructure that drastically improves post-training efficiency by decoupling generation from training. Furthermore, we propose novel asynchronous agent RL algorithms that further improve RL quality, enabling the model to learn from complex, long-horizon interactions more effectively. Through these innovations, GLM-5 achieves state-of-the-art performance on major open benchmarks. Most critically, GLM-5 demonstrates unprecedented capability in real-world coding tasks, surpassing previous baselines in handling end-to-end software engineering challenges. Code, models, and more information are available at https://github.com/zai-org/GLM-5.

### 🤖 AI 总结

**一句话总结**：GLM-5 是一代面向“Agentic Engineering”的基础模型，通过高效架构与异步强化学习基础设施，在长上下文推理与真实软件工程任务上取得了新一代 SOTA 表现。

**研究动机**：作者希望从“vibe coding”式的辅助编程升级到真正可自治执行复杂工程工作流的智能体体系，同时在保持长上下文和强推理/编码能力的前提下显著降低训练与推理成本，并提升模型在复杂长程交互中的学习能力。

**核心方法**：在模型层面采用 DSA 以在压低训练与推理成本的同时保持长上下文保真度；在训练范式上构建异步强化学习基础设施，将生成与训练解耦以提升后训练效率，并提出新的异步 agent 强化学习算法，使模型能更有效地从复杂、长时序交互中学习。

**主要结论**：GLM-5 在主要开放基准上达到或超过现有最优水平，尤其在端到端真实编码与软件工程任务中表现突出，展示了从传统代码补全向更高自治性的工程智能体迈进的能力，并已开源代码与模型以支持进一步研究与应用。

**关键词**：大语言模型, agentic workflow, agent, 深度学习, 异步强化学习, 长上下文推理, 代码生成, 软件工程助手, 自动化调试

**评分**：47

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15763v1) | [下载PDF](https://arxiv.org/pdf/2602.15763v1.pdf)

---

## [27. UrbanVerse: Learning Urban Region Representation Across Cities and Tasks](https://arxiv.org/abs/2602.15750v1)

**作者**：Fengze Sun, Egemen Tanin, Shanika Karunasekera 等 6 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-17

### 📄 论文摘要

Recent advances in urban region representation learning have enabled a wide range of applications in urban analytics, yet existing methods remain limited in their capabilities to generalize across cities and analytic tasks. We aim to generalize urban representation learning beyond city- and task-specific settings, towards a foundation-style model for urban analytics. To this end, we propose UrbanVerse, a model for cross-city urban representation learning and cross-task urban analytics. For cross-city generalization, UrbanVerse focuses on features local to the target regions and structural features of the nearby regions rather than the entire city. We model regions as nodes on a graph, which enables a random walk-based procedure to form "sequences of regions" that reflect both local and neighborhood structural features for urban region representation learning. For cross-task generalization, we propose a cross-task learning module named HCondDiffCT. This module integrates region-conditioned prior knowledge and task-conditioned semantics into the diffusion process to jointly model multiple downstream urban prediction tasks. HCondDiffCT is generic. It can also be integrated with existing urban representation learning models to enhance their downstream task effectiveness. Experiments on real-world datasets show that UrbanVerse consistently outperforms state-of-the-art methods across six tasks under cross-city settings, achieving up to 35.89% improvements in prediction accuracy.

### 🤖 AI 总结

**一句话总结**：UrbanVerse 提出了一种可跨城市、跨任务泛化的城市区域表征与预测统一框架，在多种城市分析任务上显著提升精度。

**研究动机**：现有城市区域表示方法多针对单城单任务，难以迁移到新城市或同时支持多种下游预测任务，限制了城市计算走向“基础模型”式通用能力的发展。

**核心方法**：UrbanVerse 将城市区域建模为图节点，通过随机游走生成反映局部与邻域结构的“区域序列”进行区域表征学习，并设计 HCondDiffCT 模块，将“区域条件先验知识”和“任务条件语义”注入扩散过程，实现多任务联合建模及对现有模型的可插拔增强。

**主要结论**：在真实城市数据上，UrbanVerse 在跨城设定下的六个预测任务中均优于现有方法，最高提升约 35.89% 精度，验证了该方法在跨城市迁移与跨任务统一建模方面的有效性与通用性。

**关键词**：深度学习, 图神经网络, 区域表示学习, 跨城市迁移, 多任务学习, 扩散模型, HCondDiffCT模块, 城市计算, 随机游走序列, 城市预测任务, diffusion

**评分**：39

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15750v1) | [下载PDF](https://arxiv.org/pdf/2602.15750v1.pdf)

---

## [28. MRC-GAT: A Meta-Relational Copula-Based Graph Attention Network for Interpretable Multimodal Alzheimer's Disease Diagnosis](https://arxiv.org/abs/2602.15740v1)

**作者**：Fatemeh Khalvandi, Saadat Izadi, Abdolah Chalechale  
**分类**：cs.LG, cs.AI, q-bio.QM  
**发布时间**：2026-02-17

### 📄 论文摘要

Alzheimer's disease (AD) is a progressive neurodegenerative condition necessitating early and precise diagnosis to provide prompt clinical management. Given the paramount importance of early diagnosis, recent studies have increasingly focused on computer-aided diagnostic models to enhance precision and reliability. However, most graph-based approaches still rely on fixed structural designs, which restrict their flexibility and limit generalization across heterogeneous patient data. To overcome these limitations, the Meta-Relational Copula-Based Graph Attention Network (MRC-GAT) is proposed as an efficient multimodal model for AD classification tasks. The proposed architecture, copula-based similarity alignment, relational attention, and node fusion are integrated as the core components of episodic meta-learning, such that the multimodal features, including risk factors (RF), Cognitive test scores, and MRI attributes, are first aligned via a copula-based transformation in a common statistical space and then combined by a multi-relational attention mechanism. According to evaluations performed on the TADPOLE and NACC datasets, the MRC-GAT model achieved accuracies of 96.87% and 92.31%, respectively, demonstrating state-of-the-art performance compared to existing diagnostic models. Finally, the proposed model confirms the robustness and applicability of the proposed method by providing interpretability at various stages of disease diagnosis.

### 🤖 AI 总结

**一句话总结**：论文提出了一种基于元关系与Copula对齐的图注意力网络MRC-GAT，用于多模态阿尔茨海默病诊断并兼顾高准确率与可解释性。

**研究动机**：现有基于图的AD诊断方法多依赖固定结构，难以适应异质多模态患者数据，限制了模型的泛化性和临床可用性，因此需要一种能灵活建模多模态关系且具可解释性的框架。

**核心方法**：MRC-GAT首先通过Copula变换将风险因素、认知量表和MRI等多模态特征对齐到统一统计空间，再利用多关系图注意力机制和节点融合在元学习框架下进行任务级训练，以自动学习适应不同数据分布的图结构与权重。

**主要结论**：在TADPOLE和NACC数据集上，MRC-GAT分别达到96.87%和92.31%的分类准确率，优于现有方法，并能在疾病不同阶段提供关系权重和特征贡献层面的解释性，证明了方法的有效性与鲁棒性。

**关键词**：深度学习, 图神经网络, 注意力机制, 多模态学习, 医学影像分析, 阿尔茨海默病诊断, 元学习, 特征对齐, 可解释性模型, generative

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15740v1) | [下载PDF](https://arxiv.org/pdf/2602.15740v1.pdf)

---

## [29. Random Wavelet Features for Graph Kernel Machines](https://arxiv.org/abs/2602.15711v1)

**作者**：Valentin de Bassompierre, Jean-Charles Delvenne, Laurent Jacques  
**分类**：cs.LG, cs.AI, eess.SP  
**发布时间**：2026-02-17

### 📄 论文摘要

Node embeddings map graph vertices into low-dimensional Euclidean spaces while preserving structural information. They are central to tasks such as node classification, link prediction, and signal reconstruction. A key goal is to design node embeddings whose dot products capture meaningful notions of node similarity induced by the graph. Graph kernels offer a principled way to define such similarities, but their direct computation is often prohibitive for large networks. Inspired by random feature methods for kernel approximation in Euclidean spaces, we introduce randomized spectral node embeddings whose dot products estimate a low-rank approximation of any specific graph kernel. We provide theoretical and empirical results showing that our embeddings achieve more accurate kernel approximations than existing methods, particularly for spectrally localized kernels. These results demonstrate the effectiveness of randomized spectral constructions for scalable and principled graph representation learning.

### 🤖 AI 总结

**一句话总结**：论文提出一种基于随机小波/谱特征的节点嵌入方法，用低维内积高效近似任意给定的图核，从而实现可扩展的图表示学习。

**研究动机**：传统图核能刻画有意义的节点相似性，但直接计算在大图上代价高昂；现有节点嵌入方法又难以在保持谱性质的同时精确近似特定图核。

**核心方法**：借鉴欧式空间中的随机特征思想，构造随机谱（小波式）节点嵌入，使得节点间点积估计给定图核的低秩近似，并从理论上分析近似误差，重点针对谱局部化图核。

**主要结论**：理论和实验结果表明，该随机谱节点嵌入相比现有方法能更准确地近似图核，尤其对谱局部化核优势明显，从而为大规模图上的可扩展、原则化图表示学习提供了一种有效方案。

**关键词**：深度学习, 神经网络, 图表示学习, 随机特征映射, 光谱图卷积, 节点嵌入, 图核方法, 低秩近似, 相似度度量, embedding

**评分**：26

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15711v1) | [下载PDF](https://arxiv.org/pdf/2602.15711v1.pdf)

---

## [30. Controlled oscillation modeling using port-Hamiltonian neural networks](https://arxiv.org/abs/2602.15704v1)

**作者**：Maximino Linares, Guillaume Doras, Thomas Hélie  
**分类**：cs.LG, eess.SY, math.DS  
**发布时间**：2026-02-17

### 📄 论文摘要

Learning dynamical systems through purely data-driven methods is challenging as they do not learn the underlying conservation laws that enable them to correctly generalize. Existing port-Hamiltonian neural network methods have recently been successfully applied for modeling mechanical systems. However, even though these methods are designed on power-balance principles, they usually do not consider power-preserving discretizations and often rely on Runge-Kutta numerical methods. In this work, we propose to use a second-order discrete gradient method embedded in the learning of dynamical systems with port-Hamiltonian neural networks. Numerical results are provided for three systems deliberately selected to span different ranges of dynamical behavior under control: a baseline harmonic oscillator with quadratic energy storage; a Duffing oscillator, with a non-quadratic Hamiltonian offering amplitude-dependent effects; and a self-sustained oscillator, which can stabilize in a controlled limit cycle through the incorporation of a nonlinear dissipation. We show how the use of this discrete gradient method outperforms the performance of a Runge-Kutta method of the same order. Experiments are also carried out to compare two theoretically equivalent port-Hamiltonian systems formulations and to analyze the impact of regularizing the Jacobian of port-Hamiltonian neural networks during training.

### 🤖 AI 总结

**一句话总结**：本文提出在端口哈密顿神经网络中嵌入二阶离散梯度方法，以功率守恒方式建模受控振荡系统，并在精度与泛化上优于同阶Runge-Kutta。

**研究动机**：传统数据驱动动力系统学习难以显式编码守恒律，现有端口哈密顿神经网络常用非保结构的Runge-Kutta离散，导致对能量与功率结构的刻画不足，限制了在复杂受控振荡场景中的泛化与稳定性。

**核心方法**：将二阶离散梯度时间离散方法嵌入端口哈密顿神经网络训练与推理过程，使时间步进本身满足功率平衡与能量结构保持，并在三类代表性振荡系统（线性谐振子、Duffing非线性振子、自激极限环振子）上进行对比实验，同时考察两种等价pH形式及Jacobian正则化的影响。

**主要结论**：离散梯度端口哈密顿神经网络在控制下振荡系统建模中，相比同阶Runge-Kutta具有更高预测精度与更好能量结构保持；两种等价pH表述在数值上表现存在差异，且对Jacobian进行正则化有助于提升训练稳定性与模型泛化。

**关键词**：神经网络, 深度学习, port-Hamiltonian神经网络, 动力系统建模, 受控振荡, 离散梯度方法, 数值积分, 非线性振子建模, 能量守恒约束, neural network

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2602.15704v1) | [下载PDF](https://arxiv.org/pdf/2602.15704v1.pdf)

---

