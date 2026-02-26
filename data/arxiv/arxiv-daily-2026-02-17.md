# arXiv AI 论文日报 | 2026-02-17

> 共 15 篇论文，由AI自动总结

## 📑 目录

- [cs.LG](#csLG) (8 篇)
- [cs.CL](#csCL) (2 篇)
- [cs.AI](#csAI) (4 篇)
- [cs.CV](#csCV) (1 篇)

---

## cs.AI

## [1. Improving Interactive In-Context Learning from Natural Language Feedback](https://arxiv.org/abs/2602.16066v1)

**作者**：Martin Klissarov, Jonathan Cook, Diego Antognini 等 8 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-17

### 📄 论文摘要

Adapting one's thought process based on corrective feedback is an essential ability in human learning, particularly in collaborative settings. In contrast, the current large language model training paradigm relies heavily on modeling vast, static corpora. While effective for knowledge acquisition, it overlooks the interactive feedback loops essential for models to adapt dynamically to their context. In this work, we propose a framework that treats this interactive in-context learning ability not as an emergent property, but as a distinct, trainable skill. We introduce a scalable method that transforms single-turn verifiable tasks into multi-turn didactic interactions driven by information asymmetry. We first show that current flagship models struggle to integrate corrective feedback on hard reasoning tasks. We then demonstrate that models trained with our approach dramatically improve the ability to interactively learn from language feedback. More specifically, the multi-turn performance of a smaller model nearly reaches that of a model an order of magnitude larger. We also observe robust out-of-distribution generalization: interactive training on math problems transfers to diverse domains like coding, puzzles and maze navigation. Our qualitative analysis suggests that this improvement is due to an enhanced in-context plasticity. Finally, we show that this paradigm offers a unified path to self-improvement. By training the model to predict the teacher's critiques, effectively modeling the feedback environment, we convert this external signal into an internal capability, allowing the model to self-correct even without a teacher.

### 🤖 AI 总结

**一句话总结**：论文提出将“从自然语言纠错反馈中交互式学习”作为可训练能力，通过构造多轮教学式交互进行训练，显著提升模型在多轮推理中的自我修正与跨领域迁移能力。

**研究动机**：现有大模型主要从静态语料中学习，缺少对“在协作中根据语言反馈动态调整推理过程”的系统训练，导致在困难推理任务上难以有效吸收纠错意见并改进后续回答。

**核心方法**：将单轮可验证任务扩展为由信息不对称驱动的多轮“教师-学生”纠错对话数据，训练模型在多轮中理解批评、更新解题策略并给出改进答案；进一步让模型学习预测教师的批评，从而内化反馈环境，实现无教师时的自我纠错。

**主要结论**：经交互式训练后，小模型的多轮表现几乎逼近大一个数量级的模型，并在分布外任务上稳健泛化（数学训练可迁移到编程、谜题、迷宫等）；提升主要来自更强的in-context可塑性，并为模型自我改进提供统一路径。

**关键词**：交互式上下文学习, 自然语言反馈, 纠错反馈融合, 多轮教学交互, 信息不对称任务构造, 困难推理任务, 上下文可塑性, 分布外泛化, 小模型性能追赶, 批评预测训练, 可扩展训练框架

**评分**：53

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16066v1) | [下载PDF](https://arxiv.org/pdf/2602.16066v1.pdf)

---

## [2. Evidence-Grounded Subspecialty Reasoning: Evaluating a Curated Clinical Intelligence Layer on the 2025 Endocrinology Board-Style Examination](https://arxiv.org/abs/2602.16050v1)

**作者**：Amir Hosseinian, MohammadReza Zare Shahneh, Umer Mansoor 等 6 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-02-17

### 📄 论文摘要

Background: Large language models have demonstrated strong performance on general medical examinations, but subspecialty clinical reasoning remains challenging due to rapidly evolving guidelines and nuanced evidence hierarchies. Methods: We evaluated January Mirror, an evidence-grounded clinical reasoning system, against frontier LLMs (GPT-5, GPT-5.2, Gemini-3-Pro) on a 120-question endocrinology board-style examination. Mirror integrates a curated endocrinology and cardiometabolic evidence corpus with a structured reasoning architecture to generate evidence-linked outputs. Mirror operated under a closed-evidence constraint without external retrieval. Comparator LLMs had real-time web access to guidelines and primary literature. Results: Mirror achieved 87.5% accuracy (105/120; 95% CI: 80.4-92.3%), exceeding a human reference of 62.3% and frontier LLMs including GPT-5.2 (74.6%), GPT-5 (74.0%), and Gemini-3-Pro (69.8%). On the 30 most difficult questions (human accuracy less than 50%), Mirror achieved 76.7% accuracy. Top-2 accuracy was 92.5% for Mirror versus 85.25% for GPT-5.2. Conclusions: Mirror provided evidence traceability: 74.2% of outputs cited at least one guideline-tier source, with 100% citation accuracy on manual verification. Curated evidence with explicit provenance can outperform unconstrained web retrieval for subspecialty clinical reasoning and supports auditability for clinical deployment.

### 🤖 AI 总结

**一句话总结**：该研究表明，基于策展证据库与结构化推理的临床系统 January Mirror 在2025内分泌专科板考题上显著优于具备实时联网检索的前沿LLM，并提供可审计的证据溯源。

**研究动机**：通用LLM在综合医学考试表现良好，但在指南快速更新、证据层级复杂的专科推理中仍易出错且难以审计；因此需要更“证据可追溯”的推理机制来支持临床部署。

**核心方法**：在120题内分泌板考风格试卷上对比 Mirror 与 GPT-5/GPT-5.2/Gemini-3-Pro：Mirror 在“闭卷证据约束”下仅使用内分泌与心代谢策展证据语料，并用结构化推理输出带证据链接的答案；对照LLM允许实时联网检索指南与文献。

**主要结论**：Mirror 准确率87.5%（困难题76.7%）高于人类参考与各前沿LLM（约69.8%–74.6%），Top-2准确率也更高；其输出中74.2%引用指南级来源且人工核验引用准确率100%，说明高质量策展证据+显式溯源可优于不受限的网页检索并增强临床可审计性。

**关键词**：证据驱动推理, 亚专科临床推理, 内分泌学考试评测, 封闭证据约束, 证据语料库构建, 结构化推理架构, 证据溯源, 心代谢医学, LLM基准评测, 联网检索对比

**评分**：46

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16050v1) | [下载PDF](https://arxiv.org/pdf/2602.16050v1.pdf)

---

## [3. How Uncertain Is the Grade? A Benchmark of Uncertainty Metrics for LLM-Based Automatic Assessment](https://arxiv.org/abs/2602.16039v1)

**作者**：Hang Li, Kaiqi Yang, Xianxuan Long 等 12 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-17

### 📄 论文摘要

The rapid rise of large language models (LLMs) is reshaping the landscape of automatic assessment in education. While these systems demonstrate substantial advantages in adaptability to diverse question types and flexibility in output formats, they also introduce new challenges related to output uncertainty, stemming from the inherently probabilistic nature of LLMs. Output uncertainty is an inescapable challenge in automatic assessment, as assessment results often play a critical role in informing subsequent pedagogical actions, such as providing feedback to students or guiding instructional decisions. Unreliable or poorly calibrated uncertainty estimates can lead to unstable downstream interventions, potentially disrupting students' learning processes and resulting in unintended negative consequences. To systematically understand this challenge and inform future research, we benchmark a broad range of uncertainty quantification methods in the context of LLM-based automatic assessment. Although the effectiveness of these methods has been demonstrated in many tasks across other domains, their applicability and reliability in educational settings, particularly for automatic grading, remain underexplored. Through comprehensive analyses of uncertainty behaviors across multiple assessment datasets, LLM families, and generation control settings, we characterize the uncertainty patterns exhibited by LLMs in grading scenarios. Based on these findings, we evaluate the strengths and limitations of different uncertainty metrics and analyze the influence of key factors, including model families, assessment tasks, and decoding strategies, on uncertainty estimates. Our study provides actionable insights into the characteristics of uncertainty in LLM-based automatic assessment and lays the groundwork for developing more reliable and effective uncertainty-aware grading systems in the future.

### 🤖 AI 总结

**一句话总结**：本文系统基准评测了多种不确定性量化方法在LLM自动评分中的表现，揭示不同模型、任务与解码设置下不确定性的规律与优劣。

**研究动机**：LLM用于自动评测虽灵活强大，但输出具有概率性导致评分不确定；若不确定性估计不可靠或校准差，会误导反馈与教学决策并带来负面学习影响。

**核心方法**：作者在多个评测数据集、不同LLM家族与生成控制/解码策略下，统一对比一系列不确定性指标与量化方法，分析其不确定性行为模式、稳定性与适用性，并考察关键因素对估计结果的影响。

**主要结论**：不确定性在自动评分场景中呈现明确且受模型家族、任务类型与解码策略显著影响的模式；不同不确定性指标各有优势与局限，需针对教育评分场景选择/设计更可靠、可校准的不确定性感知评分方案。

**关键词**：自动评分, 教育测评, LLM评测基准, 不确定性量化, 不确定性指标, 置信度校准, 生成解码策略, 模型家族对比, 跨数据集分析, 不确定性感知评分

**评分**：20

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16039v1) | [下载PDF](https://arxiv.org/pdf/2602.16039v1.pdf)

---

## [4. Optimization Instability in Autonomous Agentic Workflows for Clinical Symptom Detection](https://arxiv.org/abs/2602.16037v1)

**作者**：Cameron Cagan, Pedram Fard, Jiazi Tian 等 6 位作者  
**分类**：cs.AI, cs.MA  
**发布时间**：2026-02-17

### 📄 论文摘要

Autonomous agentic workflows that iteratively refine their own behavior hold considerable promise, yet their failure modes remain poorly characterized. We investigate optimization instability, a phenomenon in which continued autonomous improvement paradoxically degrades classifier performance, using Pythia, an open-source framework for automated prompt optimization. Evaluating three clinical symptoms with varying prevalence (shortness of breath at 23%, chest pain at 12%, and Long COVID brain fog at 3%), we observed that validation sensitivity oscillated between 1.0 and 0.0 across iterations, with severity inversely proportional to class prevalence. At 3% prevalence, the system achieved 95% accuracy while detecting zero positive cases, a failure mode obscured by standard evaluation metrics. We evaluated two interventions: a guiding agent that actively redirected optimization, amplifying overfitting rather than correcting it, and a selector agent that retrospectively identified the best-performing iteration successfully prevented catastrophic failure. With selector agent oversight, the system outperformed expert-curated lexicons on brain fog detection by 331% (F1) and chest pain by 7%, despite requiring only a single natural language term as input. These findings characterize a critical failure mode of autonomous AI systems and demonstrate that retrospective selection outperforms active intervention for stabilization in low-prevalence classification tasks.

### 🤖 AI 总结

**一句话总结**：论文发现自主代理式提示优化在低患病率症状检测中会出现“越优化越变差”的不稳定现象，而通过事后“选择最佳迭代”的监督可显著稳定并提升性能。

**研究动机**：自主迭代改进的agentic工作流被寄予厚望，但其失败模式未被充分刻画，尤其在临床低阳性率任务中常规指标会掩盖灾难性漏检风险。

**核心方法**：使用开源自动提示优化框架Pythia，在三种不同患病率的症状（23%、12%、3%）上多轮迭代评估敏感性/准确率等表现，并对比两种干预：主动“引导agent”纠偏与事后“选择器agent”从历史迭代中挑选最佳版本。

**主要结论**：优化过程中验证集敏感性可在0到1间剧烈振荡且低患病率更严重，甚至出现95%准确率但0阳性检出的指标陷阱；引导agent会加剧过拟合，而选择器agent能避免灾难性失败并在脑雾/胸痛检测上分别较专家词典提升F1 331%/7%。

**关键词**：临床症状检测, 自主智能体工作流, 提示词优化, 优化不稳定性, 低患病率分类, 类别不平衡, 过拟合, 回顾式选择, 智能体干预策略, 评价指标失真（准确率陷阱）

**评分**：42

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16037v1) | [下载PDF](https://arxiv.org/pdf/2602.16037v1.pdf)

---

## cs.CL

## [5. Language Statistics and False Belief Reasoning: Evidence from 41 Open-Weight LMs](https://arxiv.org/abs/2602.16085v1)

**作者**：Sean Trott, Samuel Taylor, Cameron Jones 等 5 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-02-17

### 📄 论文摘要

Research on mental state reasoning in language models (LMs) has the potential to inform theories of human social cognition--such as the theory that mental state reasoning emerges in part from language exposure--and our understanding of LMs themselves. Yet much published work on LMs relies on a relatively small sample of closed-source LMs, limiting our ability to rigorously test psychological theories and evaluate LM capacities. Here, we replicate and extend published work on the false belief task by assessing LM mental state reasoning behavior across 41 open-weight models (from distinct model families). We find sensitivity to implied knowledge states in 34% of the LMs tested; however, consistent with prior work, none fully ``explain away'' the effect in humans. Larger LMs show increased sensitivity and also exhibit higher psychometric predictive power. Finally, we use LM behavior to generate and test a novel hypothesis about human cognition: both humans and LMs show a bias towards attributing false beliefs when knowledge states are cued using a non-factive verb (``John thinks...'') than when cued indirectly (``John looks in the...''). Unlike the primary effect of knowledge states, where human sensitivity exceeds that of LMs, the magnitude of the human knowledge cue effect falls squarely within the distribution of LM effect sizes-suggesting that distributional statistics of language can in principle account for the latter but not the former in humans. These results demonstrate the value of using larger samples of open-weight LMs to test theories of human cognition and evaluate LM capacities.

### 🤖 AI 总结

**一句话总结**：跳过

**研究动机**：跳过

**核心方法**：跳过

**主要结论**：跳过

**关键词**：错误信念推理, 心智理论, 心理状态推理, 知识状态推断, 知识线索效应, 非事实性动词, 语言分布统计, 开源权重语言模型, 模型规模效应, 跨模型评测, 心理测量预测力

**评分**：12

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16085v1) | [下载PDF](https://arxiv.org/pdf/2602.16085v1.pdf)

---

## [6. A Curious Class of Adpositional Multiword Expressions in Korean](https://arxiv.org/abs/2602.16023v1)

**作者**：Junghyun Min, Na-Rae Han, Jena D. Hwang 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-02-17

### 📄 论文摘要

Multiword expressions (MWEs) have been widely studied in cross-lingual annotation frameworks such as PARSEME. However, Korean MWEs remain underrepresented in these efforts. In particular, Korean multiword adpositions lack systematic analysis, annotated resources, and integration into existing multilingual frameworks. In this paper, we study a class of Korean functional multiword expressions: postpositional verb-based constructions (PVCs). Using data from Korean Wikipedia, we survey and analyze several PVC expressions and contrast them with non-MWEs and light verb constructions (LVCs) with similar structure. Building on this analysis, we propose annotation guidelines designed to support future work in Korean multiword adpositions and facilitate alignment with cross-lingual frameworks.

### 🤖 AI 总结

**一句话总结**：论文系统考察韩语一种后置词性动词多词表达（PVCs），并提出可与跨语言框架对齐的标注指南。

**研究动机**：现有PARSEME等跨语言MWE标注框架中韩语资源与分析不足，尤其是多词介词/后置词类表达缺乏系统研究与可复用标注规范。

**核心方法**：基于韩语维基百科语料抽取并梳理多种PVC实例，分析其形式与功能特征，并与结构相近但不属于MWE的表达及轻动词结构（LVCs）进行对比，进而归纳判别标准并制定标注指南。

**主要结论**：PVCs可作为韩语功能性多词表达中的一类独立且可操作的标注对象；所提指南为构建韩语多词后置词资源、减少与非MWE/LVC混淆并与多语言标注框架衔接提供了基础。

**关键词**：韩语多词表达, 多词后置词, 后置词动词构式(PVC, 功能性多词表达, 跨语言标注框架, 轻动词构式(LVC, 韩语维基百科语料, 多词表达标注指南, 多语言框架对齐, 韩语语言资源构建

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16023v1) | [下载PDF](https://arxiv.org/pdf/2602.16023v1.pdf)

---

## cs.CV

## [7. MedProbCLIP: Probabilistic Adaptation of Vision-Language Foundation Model for Reliable Radiograph-Report Retrieval](https://arxiv.org/abs/2602.16019v1)

**作者**：Ahmad Elallaf, Yu Zhang, Yuktha Priya Masupalli 等 7 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-02-17

### 📄 论文摘要

Vision-language foundation models have emerged as powerful general-purpose representation learners with strong potential for multimodal understanding, but their deterministic embeddings often fail to provide the reliability required for high-stakes biomedical applications. This work introduces MedProbCLIP, a probabilistic vision-language learning framework for chest X-ray and radiology report representation learning and bidirectional retrieval. MedProbCLIP models image and text representations as Gaussian embeddings through a probabilistic contrastive objective that explicitly captures uncertainty and many-to-many correspondences between radiographs and clinical narratives. A variational information bottleneck mitigates overconfident predictions, while MedProbCLIP employs multi-view radiograph encoding and multi-section report encoding during training to provide fine-grained supervision for clinically aligned correspondence, yet requires only a single radiograph and a single report at inference. Evaluated on the MIMIC-CXR dataset, MedProbCLIP outperforms deterministic and probabilistic baselines, including CLIP, CXR-CLIP, and PCME++, in both retrieval and zero-shot classification. Beyond accuracy, MedProbCLIP demonstrates superior calibration, risk-coverage behavior, selective retrieval reliability, and robustness to clinically relevant corruptions, underscoring the value of probabilistic vision-language modeling for improving the trustworthiness and safety of radiology image-text retrieval systems.

### 🤖 AI 总结

**一句话总结**：MedProbCLIP将胸片与放射报告表示为带不确定性的高斯嵌入，通过概率对比学习提升检索与零样本分类的可靠性与校准性。

**研究动机**：现有视觉-语言基础模型多为确定性嵌入，难以表达医学影像-文本的多对多对应关系与不确定性，导致高风险场景下检索/预测过度自信且不可靠。

**核心方法**：提出概率对比学习框架，将图像与文本编码为高斯分布嵌入并显式建模不确定性；引入变分信息瓶颈抑制过度自信，同时训练时使用多视角胸片编码与多章节报告编码提供更细粒度监督，推理仅需单张胸片与单份报告。

**主要结论**：在MIMIC-CXR上相较CLIP、CXR-CLIP与PCME++等基线取得更优的双向检索与零样本分类表现，并在校准、风险-覆盖、选择性检索可靠性及对临床相关扰动的鲁棒性方面显著提升，表明概率化建模能增强放射检索系统的可信与安全性。

**关键词**：医学视觉-语言模型, 胸部X光, 影像-报告检索, 双向检索, 概率嵌入, 高斯嵌入, 不确定性建模, 概率对比学习, 变分信息瓶颈, 模型校准, 选择性检索, 零样本分类

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16019v1) | [下载PDF](https://arxiv.org/pdf/2602.16019v1.pdf)

---

## cs.LG

## [8. Quantifying LLM Attention-Head Stability: Implications for Circuit Universality](https://arxiv.org/abs/2602.16740v1)

**作者**：Karan Bali, Jack Stanley, Praneet Suresh 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-17

### 📄 论文摘要

In mechanistic interpretability, recent work scrutinizes transformer "circuits" - sparse, mono or multi layer sub computations, that may reflect human understandable functions. Yet, these network circuits are rarely acid-tested for their stability across different instances of the same deep learning architecture. Without this, it remains unclear whether reported circuits emerge universally across labs or turn out to be idiosyncratic to a particular estimation instance, potentially limiting confidence in safety-critical settings. Here, we systematically study stability across-refits in increasingly complex transformer language models of various sizes. We quantify, layer by layer, how similarly attention heads learn representations across independently initialized training runs. Our rigorous experiments show that (1) middle-layer heads are the least stable yet the most representationally distinct; (2) deeper models exhibit stronger mid-depth divergence; (3) unstable heads in deeper layers become more functionally important than their peers from the same layer; (4) applying weight decay optimization substantially improves attention-head stability across random model initializations; and (5) the residual stream is comparatively stable. Our findings establish the cross-instance robustness of circuits as an essential yet underappreciated prerequisite for scalable oversight, drawing contours around possible white-box monitorability of AI systems.

### 🤖 AI 总结

**一句话总结**：论文量化比较同一Transformer架构在不同随机初始化重训下的注意力头一致性，发现中层头最不稳定但最“独特”，且权重衰减能显著提升跨实例稳定性。

**研究动机**：机制可解释性常宣称发现可复用的“电路”(circuits)，但很少检验这些结构在不同训练实例间是否稳定可复现；若不稳定，白盒监控与安全结论可能只对单个模型偶然成立。

**核心方法**：对不同规模/深度的语言模型进行多次独立重训(refits)，逐层量化注意力头在表示学习上的相似度/对齐程度，并分析不稳定头的功能重要性与残差流(residual stream)的稳定性，同时对比加入weight decay等优化对稳定性的影响。

**主要结论**：中间层注意力头跨实例最不稳定但表征差异最大，且模型越深中层分化越强；深层中不稳定头往往更关键，而weight decay可显著提升注意力头稳定性，残差流整体相对稳定，提示“电路”可复现性应成为可扩展监督的前置条件。

**关键词**：机制可解释性, 注意力头稳定性, 跨重训一致性, 表征相似性评估, 中层表征分化, 深层模型分歧, 权重衰减正则化, 残差流稳定性, 白盒可监控性, 可扩展监督

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16740v1) | [下载PDF](https://arxiv.org/pdf/2602.16740v1.pdf)

---

## [9. Omni-iEEG: A Large-Scale, Comprehensive iEEG Dataset and Benchmark for Epilepsy Research](https://arxiv.org/abs/2602.16072v2)

**作者**：Chenda Duan, Yipeng Zhang, Sotaro Kanai 等 12 位作者  
**分类**：cs.LG, cs.AI, q-bio.NC  
**发布时间**：2026-02-17

### 📄 论文摘要

Epilepsy affects over 50 million people worldwide, and one-third of patients suffer drug-resistant seizures where surgery offers the best chance of seizure freedom. Accurate localization of the epileptogenic zone (EZ) relies on intracranial EEG (iEEG). Clinical workflows, however, remain constrained by labor-intensive manual review. At the same time, existing data-driven approaches are typically developed on single-center datasets that are inconsistent in format and metadata, lack standardized benchmarks, and rarely release pathological event annotations, creating barriers to reproducibility, cross-center validation, and clinical relevance. With extensive efforts to reconcile heterogeneous iEEG formats, metadata, and recordings across publicly available sources, we present $\textbf{Omni-iEEG}$, a large-scale, pre-surgical iEEG resource comprising $\textbf{302 patients}$ and $\textbf{178 hours}$ of high-resolution recordings. The dataset includes harmonized clinical metadata such as seizure onset zones, resections, and surgical outcomes, all validated by board-certified epileptologists. In addition, Omni-iEEG provides over 36K expert-validated annotations of pathological events, enabling robust biomarker studies. Omni-iEEG serves as a bridge between machine learning and epilepsy research. It defines clinically meaningful tasks with unified evaluation metrics grounded in clinical priors, enabling systematic evaluation of models in clinically relevant settings. Beyond benchmarking, we demonstrate the potential of end-to-end modeling on long iEEG segments and highlight the transferability of representations pretrained on non-neurophysiological domains. Together, these contributions establish Omni-iEEG as a foundation for reproducible, generalizable, and clinically translatable epilepsy research. The project page with dataset and code links is available at omni-ieeg.github.io/omni-ieeg.

### 🤖 AI 总结

**一句话总结**：Omni-iEEG整合多来源术前颅内脑电数据与专家标注，提供大规模标准化数据集与临床相关基准任务以推动可复现、可泛化的癫痫AI研究。

**研究动机**：现有iEEG研究多依赖单中心数据，格式/元数据不一致且缺少标准基准与病理事件标注，导致模型难以复现、跨中心验证与临床转化。临床EZ定位仍高度依赖人工阅片，亟需规模化、结构化资源支撑自动化方法。

**核心方法**：作者对公开iEEG资源进行异构格式与元数据对齐，构建含302例患者、178小时高分辨率记录的Omni-iEEG，并由认证癫痫专家统一校验临床元数据（SOZ、切除区、术后结局）与36K+病理事件标注。基于临床先验定义统一评测指标与基准任务，并展示长片段端到端建模及跨域预训练表征的可迁移性。

**主要结论**：Omni-iEEG通过标准化数据、丰富临床元信息和大规模专家标注，显著降低跨数据源研究门槛并提升评测一致性。实验表明在临床设定下可系统比较模型，且长程建模与跨域预训练对iEEG任务具有潜力，为更具临床可译性的癫痫研究奠定基础。

**关键词**：颅内脑电（iEEG）, 癫痫手术评估, 致痫区定位, 发作起始区（SOZ）, 病理事件标注, 临床元数据标准化, 跨中心数据整合, 癫痫生物标志物, 统一评测基准, 长时序端到端建模, 迁移学习预训练表征

**评分**：38

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16072v2) | [下载PDF](https://arxiv.org/pdf/2602.16072v2.pdf)

---

## [10. Real-time Secondary Crash Likelihood Prediction Excluding Post Primary Crash Features](https://arxiv.org/abs/2602.16739v1)

**作者**：Lei Han, Mohamed Abdel-Aty, Zubayer Islam 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-17

### 📄 论文摘要

Secondary crash likelihood prediction is a critical component of an active traffic management system to mitigate congestion and adverse impacts caused by secondary crashes. However, existing approaches mainly rely on post-crash features (e.g., crash type and severity) that are rarely available in real time, limiting their practical applicability. To address this limitation, we propose a hybrid secondary crash likelihood prediction framework that does not depend on post-crash features. A dynamic spatiotemporal window is designed to extract real-time traffic flow and environmental features from primary crash locations and their upstream segments. The framework includes three models: a primary crash model to estimate the likelihood of secondary crash occurrence, and two secondary crash models to evaluate traffic conditions at crash and upstream segments under different comparative scenarios. An ensemble learning strategy integrating six machine learning algorithms is developed to enhance predictive performance, and a voting-based mechanism combines the outputs of the three models. Experiments on Florida freeways demonstrate that the proposed hybrid framework correctly identifies 91% of secondary crashes with a low false alarm rate of 0.20. The Area Under the ROC Curve improves from 0.654, 0.744, and 0.902 for the individual models to 0.952 for the hybrid model, outperforming previous studies.

### 🤖 AI 总结

**一句话总结**：提出一种不依赖事故后特征的实时二次事故风险预测混合框架，通过集成学习与投票融合显著提升预测性能。

**研究动机**：现有二次事故预测多依赖事故类型、严重度等“事后特征”，难以在事故发生后第一时间获取，导致实时应用受限。

**核心方法**：设计动态时空窗口，从主事故点及其上游路段提取实时交通流与环境特征；构建1个主事故模型+2个二次事故模型，并用6种机器学习算法做集成学习，最后以投票机制融合三模型输出。

**主要结论**：在佛罗里达高速实验中，混合模型以0.20的较低误报率识别出91%的二次事故，AUC从单模型的0.654/0.744/0.902提升至0.952，整体优于以往研究。

**关键词**：二次事故风险预测, 主动交通管理, 实时预测, 动态时空窗口, 交通流特征, 环境特征, 上游路段分析, 事后特征剔除, 集成学习, 投票融合, 高速公路事故数据

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16739v1) | [下载PDF](https://arxiv.org/pdf/2602.16739v1.pdf)

---

## [11. Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training](https://arxiv.org/abs/2602.16065v1)

**作者**：Kevin Wang, Hongqian Niu, Didong Li  
**分类**：cs.LG, cs.AI, math.ST, stat.ML  
**发布时间**：2026-02-17

### 📄 论文摘要

Generative Artificial Intelligence (AI), such as large language models (LLMs), has become a transformative force across science, industry, and society. As these systems grow in popularity, web data becomes increasingly interwoven with this AI-generated material and it is increasingly difficult to separate them from naturally generated content. As generative models are updated regularly, later models will inevitably be trained on mixtures of human-generated data and AI-generated data from earlier versions, creating a recursive training process with data contamination. Existing theoretical work has examined only highly simplified settings, where both the real data and the generative model are discrete or Gaussian, where it has been shown that such recursive training leads to model collapse. However, real data distributions are far more complex, and modern generative models are far more flexible than Gaussian and linear mechanisms. To fill this gap, we study recursive training in a general framework with minimal assumptions on the real data distribution and allow the underlying generative model to be a general universal approximator. In this framework, we show that contaminated recursive training still converges, with a convergence rate equal to the minimum of the baseline model's convergence rate and the fraction of real data used in each iteration. To the best of our knowledge, this is the first (positive) theoretical result on recursive training without distributional assumptions on the data. We further extend the analysis to settings where sampling bias is present in data collection and support all theoretical results with empirical studies.

### 🤖 AI 总结

**一句话总结**：论文研究生成模型在“递归训练+数据被旧模型生成内容污染”的现实场景下是否仍能稳定学习，并给出在极弱分布假设下仍可收敛的理论保证。

**研究动机**：随着LLM等生成式AI内容渗入互联网，新模型训练数据不可避免混入旧模型生成文本，既有理论多在离散/高斯等简化设定下得到“模型崩溃”结论，难以解释真实复杂分布与强模型能力下的行为。

**核心方法**：提出一个对真实数据分布几乎不作假设、并将生成模型视为通用逼近器的递归训练框架；分析每轮混入一定比例真实数据时的收敛性与速率，并进一步扩展到存在采样偏差的数据收集情形，同时用实验验证理论结论。

**主要结论**：在该一般框架下，污染的递归训练依然收敛，其收敛速率由“基础训练算法的速率”和“每轮真实数据占比”两者的较小者决定；此外在存在采样偏差时仍可得到相应的理论保证，并有实验支持。

**关键词**：递归训练, 数据污染, 合成数据混入, 人类数据比例, 收敛性保证, 收敛速率分析, 分布无关理论, 模型坍塌, 采样偏差

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16065v1) | [下载PDF](https://arxiv.org/pdf/2602.16065v1.pdf)

---

## [12. Extracting and Analyzing Rail Crossing Behavior Signatures from Videos using Tensor Methods](https://arxiv.org/abs/2602.16057v2)

**作者**：Dawon Ahn, Het Patel, Aemal Khattak 等 5 位作者  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-02-17

### 📄 论文摘要

Railway crossings present complex safety challenges where driver behavior varies by location, time, and conditions. Traditional approaches analyze crossings individually, limiting the ability to identify shared behavioral patterns across locations. We propose a multi-view tensor decomposition framework that captures behavioral similarities across three temporal phases: Approach (warning activation to gate lowering), Waiting (gates down to train passage), and Clearance (train passage to gate raising). We analyze railway crossing videos from multiple locations using TimeSformer embeddings to represent each phase. By constructing phase-specific similarity matrices and applying non-negative symmetric CP decomposition, we discover latent behavioral components with distinct temporal signatures. Our tensor analysis reveals that crossing location appears to be a stronger determinant of behavior patterns than time of day, and that approach-phase behavior provides particularly discriminative signatures. Visualization of the learned component space confirms location-based clustering, with certain crossings forming distinct behavioral clusters. This automated framework enables scalable pattern discovery across multiple crossings, providing a foundation for grouping locations by behavioral similarity to inform targeted safety interventions.

### 🤖 AI 总结

**一句话总结**：提出一种基于多视角张量分解的框架，从多地点铁路道口视频中自动提取并比较三阶段（接近/等待/清空）的驾驶行为签名，以发现跨地点共享的潜在行为模式。

**研究动机**：传统道口安全分析多为逐点研究，难以系统性发现不同地点之间可迁移的共性行为规律，从而限制规模化、针对性的安全干预设计。

**核心方法**：将视频按接近、等待、清空三阶段切分，并用TimeSformer提取各阶段嵌入表示；构建阶段特定的相似度矩阵后，采用非负对称CP张量分解挖掘具有时间阶段签名的潜在行为组件，并在组件空间中可视化聚类关系。

**主要结论**：结果显示道口“地点”对行为模式的决定性强于“时间段”，且接近阶段的行为特征最具区分度；学习到的组件空间呈现明显的基于地点的聚类，一些道口形成独特的行为簇，可用于按行为相似性分组以支持更精准的安全干预。

**关键词**：铁路道口安全, 驾驶行为分析, 视频行为特征, 多视角张量分解, 非负对称CP分解, 相似度矩阵构建, 时序阶段建模, 潜在行为组件, 位置驱动聚类

**评分**：26

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16057v2) | [下载PDF](https://arxiv.org/pdf/2602.16057v2.pdf)

---

## [13. Multi-Objective Alignment of Language Models for Personalized Psychotherapy](https://arxiv.org/abs/2602.16053v1)

**作者**：Mehrab Beikzadeh, Yasaman Asadollah Salmanpour, Ashima Suvarna 等 7 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-02-17

### 📄 论文摘要

Mental health disorders affect over 1 billion people worldwide, yet access to care remains limited by workforce shortages and cost constraints. While AI systems show therapeutic promise, current alignment approaches optimize objectives independently, failing to balance patient preferences with clinical safety. We survey 335 individuals with lived mental health experience to collect preference rankings across therapeutic dimensions, then develop a multi-objective alignment framework using direct preference optimization. We train reward models for six criteria -- empathy, safety, active listening, self-motivated change, trust/rapport, and patient autonomy -- and systematically compare multi-objective approaches against single-objective optimization, supervised fine-tuning, and parameter merging. Multi-objective DPO (MODPO) achieves superior balance (77.6% empathy, 62.6% safety) compared to single-objective optimization (93.6% empathy, 47.8% safety), and therapeutic criteria outperform general communication principles by 17.2%. Blinded clinician evaluation confirms MODPO is consistently preferred, with LLM-evaluator agreement comparable to inter-clinician reliability.

### 🤖 AI 总结

**一句话总结**：论文提出一种面向个性化心理治疗对话的多目标对齐框架（MODPO），在同一模型中更好地平衡同理心与临床安全等多项治疗目标。

**研究动机**：现有对齐方法多将同理心、安全等目标分开单独优化，容易出现“高同理心但低安全”等失衡，难以同时满足患者偏好与临床约束。

**核心方法**：通过对335名有心理健康经历的受访者收集多维度偏好排序，分别训练涵盖同理心、安全、积极倾听、自主改变、信任/关系、患者自主性六项标准的奖励模型，并基于直接偏好优化构建多目标DPO，与单目标优化、SFT和参数合并等方法系统对比。

**主要结论**：多目标DPO在同理心与安全等指标上取得更均衡的结果（如77.6%同理心、62.6%安全），显著优于单目标优化的失衡表现；以“治疗维度”对齐比通用沟通原则提升约17.2%，且盲测临床医生更偏好MODPO，LLM评估器与医生一致性接近医生间一致性。

**关键词**：多目标对齐, 直接偏好优化（DPO）, 奖励模型, 偏好学习, 心理治疗对话, 个性化心理健康, 临床安全, 主动倾听, 患者自主性, 临床评测一致性

**评分**：44

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16053v1) | [下载PDF](https://arxiv.org/pdf/2602.16053v1.pdf)

---

## [14. AI-CARE: Carbon-Aware Reporting Evaluation Metric for AI Models](https://arxiv.org/abs/2602.16042v2)

**作者**：KC Santosh, Srikanth Baride, Rodrigue Rizk  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-17

### 📄 论文摘要

As machine learning (ML) continues its rapid expansion, the environmental cost of model training and inference has become a critical societal concern. Existing benchmarks overwhelmingly focus on standard performance metrics such as accuracy, BLEU, or mAP, while largely ignoring energy consumption and carbon emissions. This single-objective evaluation paradigm is increasingly misaligned with the practical requirements of large-scale deployment, particularly in energy-constrained environments such as mobile devices, developing regions, and climate-aware enterprises. In this paper, we propose AI-CARE, an evaluation tool for reporting energy consumption, and carbon emissions of ML models. In addition, we introduce the carbon-performance tradeoff curve, an interpretable tool that visualizes the Pareto frontier between performance and carbon cost. We demonstrate, through theoretical analysis and empirical validation on representative ML workloads, that carbon-aware benchmarking changes the relative ranking of models and encourages architectures that are simultaneously accurate and environmentally responsible. Our proposal aims to shift the research community toward transparent, multi-objective evaluation and align ML progress with global sustainability goals. The tool and documentation are available at https://github.com/USD-AI-ResearchLab/ai-care.

### 🤖 AI 总结

**一句话总结**：AI-CARE 提出一种将能耗与碳排纳入模型评测与报告的工具，并用“碳-性能权衡曲线”展示性能与碳成本的帕累托最优关系，推动多目标可持续评估。

**研究动机**：现有 ML 基准主要关注准确率等单一性能指标，忽视训练/推理的能耗与碳排，导致在能源受限或强调气候责任的真实部署场景中评估失真。

**核心方法**：作者设计 AI-CARE 用于统一记录与报告模型的能耗和碳排，并提出碳-性能权衡曲线以可视化性能与碳成本的帕累托前沿，从而进行碳感知的模型对比与排名。

**主要结论**：理论与实验表明，引入碳感知基准会改变模型相对排名，并激励同时兼顾准确性与环境责任的架构选择，从而促使社区走向透明的多目标评估。

**关键词**：碳感知评测, 能耗计量, 碳排放核算, 多目标评估, 帕累托前沿, 性能-碳权衡曲线, 模型基准测试, 绿色AI, 训练与推理成本, 模型排名重评估

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16042v2) | [下载PDF](https://arxiv.org/pdf/2602.16042v2.pdf)

---

## [15. MolCrystalFlow: Molecular Crystal Structure Prediction via Flow Matching](https://arxiv.org/abs/2602.16020v1)

**作者**：Cheng Zeng, Harry W. Sullivan, Thomas Egg 等 11 位作者  
**分类**：cs.LG, cond-mat.mtrl-sci  
**发布时间**：2026-02-17

### 📄 论文摘要

Molecular crystal structure prediction represents a grand challenge in computational chemistry due to large sizes of constituent molecules and complex intra- and intermolecular interactions. While generative modeling has revolutionized structure discovery for molecules, inorganic solids, and metal-organic frameworks, extending such approaches to fully periodic molecular crystals is still elusive. Here, we present MolCrystalFlow, a flow-based generative model for molecular crystal structure prediction. The framework disentangles intramolecular complexity from intermolecular packing by embedding molecules as rigid bodies and jointly learning the lattice matrix, molecular orientations, and centroid positions. Centroids and orientations are represented on their native Riemannian manifolds, allowing geodesic flow construction and graph neural network operations that respects geometric symmetries. We benchmark our model against state-of-the-art generative models for large-size periodic crystals and rule-based structure generation methods on two open-source molecular crystal datasets. We demonstrate an integration of MolCrystalFlow model with universal machine learning potential to accelerate molecular crystal structure prediction, paving the way for data-driven generative discovery of molecular crystals.

### 🤖 AI 总结

**一句话总结**：MolCrystalFlow 提出一种基于流匹配的生成模型，将分子视作刚体并联合生成晶格与分子堆积，从而实现周期性分子晶体结构预测。

**研究动机**：分子晶体结构预测因分子尺寸大、分子内/分子间相互作用复杂而困难，现有生成模型难以直接扩展到完全周期的分子晶体。作者希望用数据驱动的生成式方法，在保持几何对称与周期性的前提下高效探索可行晶体结构。

**核心方法**：将分子内自由度与分子间堆积分离：把每个分子嵌入为刚体，联合学习晶格矩阵、分子取向和质心位置；并在质心/取向的原生黎曼流形上构造测地“流匹配”，结合图神经网络进行满足对称性的等变建模。

**主要结论**：在两个开源分子晶体数据集上，MolCrystalFlow 相比现有生成模型与规则法表现更优；与通用机器学习势能结合可加速结构预测流程，展示了用于分子晶体生成发现的可行路径。

**关键词**：分子晶体结构预测, 周期性晶体生成, 流匹配生成模型, 流式生成建模, 刚体分子嵌入, 晶格矩阵学习, 分子取向建模, 质心位置建模, 黎曼流形表示, 测地流构造, 图神经网络, 机器学习势能

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2602.16020v1) | [下载PDF](https://arxiv.org/pdf/2602.16020v1.pdf)

---

