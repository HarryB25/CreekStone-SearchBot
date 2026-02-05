# arXiv AI 论文日报 | 2026-02-04

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.LG](#csLG) (17 篇)
- [cs.CV](#csCV) (7 篇)
- [cs.CL](#csCL) (3 篇)
- [cs.AI](#csAI) (3 篇)

---

## cs.AI

## [1. Group-Evolving Agents: Open-Ended Self-Improvement via Experience Sharing](https://arxiv.org/abs/2602.04837v1)

**作者**：Zhaotian Weng, Antonis Antoniades, Deepak Nathani 等 6 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-04

### 📄 论文摘要

Open-ended self-improving agents can autonomously modify their own structural designs to advance their capabilities and overcome the limits of pre-defined architectures, thus reducing reliance on human intervention. We introduce Group-Evolving Agents (GEA), a new paradigm for open-ended self-improvements, which treats a group of agents as the fundamental evolutionary unit, enabling explicit experience sharing and reuse within the group throughout evolution. Unlike existing open-ended self-evolving paradigms that adopt tree-structured evolution, GEA overcomes the limitation of inefficient utilization of exploratory diversity caused by isolated evolutionary branches. We evaluate GEA on challenging coding benchmarks, where it significantly outperforms state-of-the-art self-evolving methods (71.0% vs. 56.7% on SWE-bench Verified, 88.3% vs. 68.3% on Polyglot) and matches or exceeds top human-designed agent frameworks (71.8% and 52.0% on two benchmarks, respectively). Analysis reveals that GEA more effectively converts early-stage exploratory diversity into sustained, long-term progress, achieving stronger performance under the same number of evolved agents. Furthermore, GEA exhibits consistent transferability across different coding models and greater robustness, fixing framework-level bugs in 1.4 iterations on average, versus 5 for self-evolving methods.

### 🤖 AI 总结

**一句话总结**：提出了一种新颖的群体进化代理（GEA）框架，通过经验共享实现开放式自我改进，显著提升了性能和适应性。

**研究动机**：现有自我进化代理受限于预定义架构，无法高效利用探索多样性，因此需要一种新方法以促进自主进化和能力提升。

**核心方法**：GEA将代理视为基本的进化单元，通过群体内的显性经验共享和重用，克服了树状进化结构的局限性。

**主要结论**：GEA在多个编码基准测试中表现优越，能够更有效地将早期探索多样性转化为长期进展，并在不同编码模型中展示出更强的转移性和鲁棒性。

**关键词**：自我改进, 代理, 经验共享, 进化, 机器学习, 编码基准, 结构设计, 进化单元, 性能提升, GEA, agent

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2602.04837v1) | [下载PDF](https://arxiv.org/pdf/2602.04837v1.pdf)

---

## [2. Are AI Capabilities Increasing Exponentially? A Competing Hypothesis](https://arxiv.org/abs/2602.04836v1)

**作者**：Haosen Ge, Hamsa Bastani, Osbert Bastani  
**分类**：cs.AI  
**发布时间**：2026-02-04

### 📄 论文摘要

Rapidly increasing AI capabilities have substantial real-world consequences, ranging from AI safety concerns to labor market consequences. The Model Evaluation & Threat Research (METR) report argues that AI capabilities have exhibited exponential growth since 2019. In this note, we argue that the data does not support exponential growth, even in shorter-term horizons. Whereas the METR study claims that fitting sigmoid/logistic curves results in inflection points far in the future, we fit a sigmoid curve to their current data and find that the inflection point has already passed. In addition, we propose a more complex model that decomposes AI capabilities into base and reasoning capabilities, exhibiting individual rates of improvement. We prove that this model supports our hypothesis that AI capabilities will exhibit an inflection point in the near future. Our goal is not to establish a rigorous forecast of our own, but to highlight the fragility of existing forecasts of exponential growth.

### 🤖 AI 总结

**一句话总结**：本文质疑AI能力是否呈指数增长，提出现有数据支持的模型与METR报告不同。

**研究动机**：随着AI能力的快速提升，理解其增长模式对安全性和劳动力市场具有重要意义。

**核心方法**：本文采用拟合sigmoid曲线的方法，分析AI能力的基础与推理能力，并提出更复杂的模型。

**主要结论**：研究表明AI能力的拐点已过去，未来将表现出不同的增长模式，现有的指数增长预测存在脆弱性。

**关键词**：AI能力, 机器学习, 深度学习, 神经网络, 模型评估, 劳动力市场, 安全性问题, 推理能力, 复杂模型, 预测模型

**评分**：42

**论文链接**：[查看原文](https://arxiv.org/abs/2602.04836v1) | [下载PDF](https://arxiv.org/pdf/2602.04836v1.pdf)

---

## [3. Agentic AI in Healthcare & Medicine: A Seven-Dimensional Taxonomy for Empirical Evaluation of LLM-based Agents](https://arxiv.org/abs/2602.04813v1)

**作者**：Shubham Vatsal, Harsh Dubey, Aditi Singh  
**分类**：cs.AI, cs.CY  
**发布时间**：2026-02-04

### 📄 论文摘要

Large Language Model (LLM)-based agents that plan, use tools and act has begun to shape healthcare and medicine. Reported studies demonstrate competence on various tasks ranging from EHR analysis and differential diagnosis to treatment planning and research workflows. Yet the literature largely consists of overviews which are either broad surveys or narrow dives into a single capability (e.g., memory, planning, reasoning), leaving healthcare work without a common frame. We address this by reviewing 49 studies using a seven-dimensional taxonomy: Cognitive Capabilities, Knowledge Management, Interaction Patterns, Adaptation & Learning, Safety & Ethics, Framework Typology and Core Tasks & Subtasks with 29 operational sub-dimensions. Using explicit inclusion and exclusion criteria and a labeling rubric (Fully Implemented, Partially Implemented, Not Implemented), we map each study to the taxonomy and report quantitative summaries of capability prevalence and co-occurrence patterns. Our empirical analysis surfaces clear asymmetries. For instance, the External Knowledge Integration sub-dimension under Knowledge Management is commonly realized (~76% Fully Implemented) whereas Event-Triggered Activation sub-dimenison under Interaction Patterns is largely absent (~92% Not Implemented) and Drift Detection & Mitigation sub-dimension under Adaptation & Learning is rare (~98% Not Implemented). Architecturally, Multi-Agent Design sub-dimension under Framework Typology is the dominant pattern (~82% Fully Implemented) while orchestration layers remain mostly partial. Across Core Tasks & Subtasks, information centric capabilities lead e.g., Medical Question Answering & Decision Support and Benchmarking & Simulation, while action and discovery oriented areas such as Treatment Planning & Prescription still show substantial gaps (~59% Not Implemented).

### 🤖 AI 总结

**一句话总结**：本文提出了一种七维分类法，用于评估基于大型语言模型的医疗保健代理的能力，揭示了当前文献中的能力不均衡现象。

**研究动机**：尽管已有研究显示LLM代理在医疗领域的多种任务中表现出色，但缺乏一个统一的框架来系统评估其能力。

**核心方法**：通过回顾49项研究，使用七维分类法对能力进行量化分析，并运用明确的纳入和排除标准及标签规则进行映射。

**主要结论**：分析结果显示，知识管理中的外部知识整合较为常见，而适应与学习中的漂移检测和缓解则极为稀缺，整体上信息中心能力在核心任务中占主导地位。

**关键词**：智能代理, 大语言模型, 医疗, 知识管理, 交互模式, 自适应学习, 多代理设计, 信息中心能力, 任务规划, llm

**评分**：68

**论文链接**：[查看原文](https://arxiv.org/abs/2602.04813v1) | [下载PDF](https://arxiv.org/pdf/2602.04813v1.pdf)

---

## cs.CL

## [4. CoT is Not the Chain of Truth: An Empirical Internal Analysis of Reasoning LLMs for Fake News Generation](https://arxiv.org/abs/2602.04856v1)

**作者**：Zhao Tong, Chunlin Gong, Yiping Zhang 等 8 位作者  
**分类**：cs.CL  
**发布时间**：2026-02-04

### 📄 论文摘要

From generating headlines to fabricating news, the Large Language Models (LLMs) are typically assessed by their final outputs, under the safety assumption that a refusal response signifies safe reasoning throughout the entire process. Challenging this assumption, our study reveals that during fake news generation, even when a model rejects a harmful request, its Chain-of-Thought (CoT) reasoning may still internally contain and propagate unsafe narratives. To analyze this phenomenon, we introduce a unified safety-analysis framework that systematically deconstructs CoT generation across model layers and evaluates the role of individual attention heads through Jacobian-based spectral metrics. Within this framework, we introduce three interpretable measures: stability, geometry, and energy to quantify how specific attention heads respond or embed deceptive reasoning patterns. Extensive experiments on multiple reasoning-oriented LLMs show that the generation risk rise significantly when the thinking mode is activated, where the critical routing decisions concentrated in only a few contiguous mid-depth layers. By precisely identifying the attention heads responsible for this divergence, our work challenges the assumption that refusal implies safety and provides a new understanding perspective for mitigating latent reasoning risks.

### 🤖 AI 总结

**一句话总结**：本研究揭示了大型语言模型在生成假新闻时，即使拒绝有害请求，其思维链推理仍可能传播不安全的叙事。

**研究动机**：研究者质疑传统假设，即拒绝响应可以保证整个过程的安全推理，特别是在假新闻生成的背景下。

**核心方法**：提出一个统一的安全分析框架，系统性地解构思维链生成，并通过雅可比谱度量评估个别注意力头的作用，使用稳定性、几何和能量等可解释性度量来量化欺骗性推理模式的嵌入。

**主要结论**：研究表明，思维模式激活时生成风险显著上升，关键的路由决策集中在少数中层，挑战了拒绝即安全的假设，并为减轻潜在推理风险提供了新视角。

**关键词**：生成模型, 大语言模型, 生成新闻, 逻辑推理, 注意力机制, 安全分析, Chain-of-Thought, 模型层级, 反向传播, 风险评估

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.04856v1) | [下载PDF](https://arxiv.org/pdf/2602.04856v1.pdf)

---

## [5. Decomposed Prompting Does Not Fix Knowledge Gaps, But Helps Models Say "I Don't Know"](https://arxiv.org/abs/2602.04853v1)

**作者**：Dhruv Madhwal, Lyuxin David Zhang, Dan Roth 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-02-04

### 📄 论文摘要

Large language models often struggle to recognize their knowledge limits in closed-book question answering, leading to confident hallucinations. While decomposed prompting is typically used to improve accuracy, we investigate its impact on reliability. We evaluate three task-equivalent prompting regimes: Direct, Assistive, and Incremental, across different model scales and multi-hop QA benchmarks. We find that although accuracy gains from decomposition diminish in frontier models, disagreements between prompting regimes remain highly indicative of potential errors. Because factual knowledge is stable while hallucinations are stochastic, cross-regime agreement provides a precise signal of internal uncertainty. We leverage this signal to implement a training-free abstention policy that requires no retrieval or fine-tuning. Our results show that disagreement-based abstention outperforms standard uncertainty baselines as an error detector, improving both F1 and AUROC across settings. This demonstrates that decomposition-based prompting can serve as a practical diagnostic probe for model reliability in closed-book QA.

### 🤖 AI 总结

**一句话总结**：分解提示并不能解决知识缺口，但能帮助模型更好地表达不确定性。

**研究动机**：大语言模型在闭卷问答中常常无法识别知识的局限性，导致自信的虚构回答，因此需要提高模型的可靠性。

**核心方法**：研究评估了直接、辅助和增量三种任务等效的提示方式，分析其对模型准确性和内部不确定性的影响。

**主要结论**：基于不一致性的拒绝策略在检测错误上优于传统的不确定性基线，证明了分解提示可以作为模型可靠性的有效诊断工具。

**关键词**：大语言模型, 知识限制, 问答, 提示策略, 准确性, 可靠性, 训练-free, 不确定性, 模型评估, multi-hop QA, rag

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.04853v1) | [下载PDF](https://arxiv.org/pdf/2602.04853v1.pdf)

---

## [6. SE-Bench: Benchmarking Self-Evolution with Knowledge Internalization](https://arxiv.org/abs/2602.04811v1)

**作者**：Jiarui Yuan, Tailin Jin, Weize Chen 等 6 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-02-04

### 📄 论文摘要

True self-evolution requires agents to act as lifelong learners that internalize novel experiences to solve future problems. However, rigorously measuring this foundational capability is hindered by two obstacles: the entanglement of prior knowledge, where ``new'' knowledge may appear in pre-training data, and the entanglement of reasoning complexity, where failures may stem from problem difficulty rather than an inability to recall learned knowledge. We introduce SE-Bench, a diagnostic environment that obfuscates the NumPy library and its API doc into a pseudo-novel package with randomized identifiers. Agents are trained to internalize this package and evaluated on simple coding tasks without access to documentation, yielding a clean setting where tasks are trivial with the new API doc but impossible for base models without it. Our investigation reveals three insights: (1) the Open-Book Paradox, where training with reference documentation inhibits retention, requiring "Closed-Book Training" to force knowledge compression into weights; (2) the RL Gap, where standard RL fails to internalize new knowledge completely due to PPO clipping and negative gradients; and (3) the viability of Self-Play for internalization, proving models can learn from self-generated, noisy tasks when coupled with SFT, but not RL. Overall, SE-Bench establishes a rigorous diagnostic platform for self-evolution with knowledge internalization. Our code and dataset can be found at https://github.com/thunlp/SE-Bench.

### 🤖 AI 总结

**一句话总结**：SE-Bench是一个用于评估自我进化与知识内化能力的基准测试环境。

**研究动机**：研究旨在解决自我进化能力评估中的知识纠缠和推理复杂性问题。

**核心方法**：通过将NumPy库混淆为伪新包并随机化标识符，训练代理在没有文档的情况下完成编码任务。

**主要结论**：研究发现关闭书本训练更有效，标准强化学习无法完全内化新知识，而自我对弈结合SFT能够促进内化。

**关键词**：自我进化, 知识内化, 代理, 终身学习, 训练, 评估, 编码任务, 自我生成任务, SFT

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2602.04811v1) | [下载PDF](https://arxiv.org/pdf/2602.04811v1.pdf)

---

## cs.CV

## [7. CoWTracker: Tracking by Warping instead of Correlation](https://arxiv.org/abs/2602.04877v1)

**作者**：Zihang Lai, Eldar Insafutdinov, Edgar Sucar 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-04

### 📄 论文摘要

Dense point tracking is a fundamental problem in computer vision, with applications ranging from video analysis to robotic manipulation. State-of-the-art trackers typically rely on cost volumes to match features across frames, but this approach incurs quadratic complexity in spatial resolution, limiting scalability and efficiency. In this paper, we propose \method, a novel dense point tracker that eschews cost volumes in favor of warping. Inspired by recent advances in optical flow, our approach iteratively refines track estimates by warping features from the target frame to the query frame based on the current estimate. Combined with a transformer architecture that performs joint spatiotemporal reasoning across all tracks, our design establishes long-range correspondences without computing feature correlations. Our model is simple and achieves state-of-the-art performance on standard dense point tracking benchmarks, including TAP-Vid-DAVIS, TAP-Vid-Kinetics, and Robo-TAP. Remarkably, the model also excels at optical flow, sometimes outperforming specialized methods on the Sintel, KITTI, and Spring benchmarks. These results suggest that warping-based architectures can unify dense point tracking and optical flow estimation.

### 🤖 AI 总结

**一句话总结**：提出了一种新的稠密点跟踪器CoWTracker，通过变形而非相关性匹配来提高效率和性能。

**研究动机**：现有的稠密点跟踪方法依赖于成本体积，导致在空间分辨率下的复杂度过高，限制了其可扩展性和效率。

**核心方法**：CoWTracker通过基于当前估计的变形来迭代精炼轨迹估计，并结合变压器架构进行联合时空推理，以建立长距离对应关系。

**主要结论**：该模型在标准稠密点跟踪基准上表现优异，同时在光流估计方面也超过了一些专门的方法，显示了变形架构在这两个领域的统一潜力。

**关键词**：深度学习, 计算机视觉, 变换器, 特征匹配, 光流估计, dense point tracking, spatiotemporal reasoning, optical flow, 轨迹估计, transformer

**评分**：68

**论文链接**：[查看原文](https://arxiv.org/abs/2602.04877v1) | [下载PDF](https://arxiv.org/pdf/2602.04877v1.pdf)

---

## [8. PerpetualWonder: Long-Horizon Action-Conditioned 4D Scene Generation](https://arxiv.org/abs/2602.04876v1)

**作者**：Jiahao Zhan, Zizhang Li, Hong-Xing Yu 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-04

### 📄 论文摘要

We introduce PerpetualWonder, a hybrid generative simulator that enables long-horizon, action-conditioned 4D scene generation from a single image. Current works fail at this task because their physical state is decoupled from their visual representation, which prevents generative refinements to update the underlying physics for subsequent interactions. PerpetualWonder solves this by introducing the first true closed-loop system. It features a novel unified representation that creates a bidirectional link between the physical state and visual primitives, allowing generative refinements to correct both the dynamics and appearance. It also introduces a robust update mechanism that gathers supervision from multiple viewpoints to resolve optimization ambiguity. Experiments demonstrate that from a single image, PerpetualWonder can successfully simulate complex, multi-step interactions from long-horizon actions, maintaining physical plausibility and visual consistency.

### 🤖 AI 总结

**一句话总结**：PerpetualWonder是一个混合生成模拟器，可以从单张图像生成长期、基于动作的4D场景。

**研究动机**：现有方法无法实现长期的、基于动作的场景生成，因为物理状态与视觉表现脱节，影响后续交互的生成优化。

**核心方法**：PerpetualWonder引入了首个真正的闭环系统，采用统一表示法建立物理状态与视觉原始元素之间的双向联系，并通过多视角监督机制解决优化模糊性。

**主要结论**：实验表明，PerpetualWonder能够从单一图像成功模拟复杂的多步交互，保持物理合理性和视觉一致性。

**关键词**：生成模型, 生成模拟器, 长期预测, 4D场景生成, 物理状态, 视觉表示, 反馈机制, 多视角监督, 人机交互, generative

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.04876v1) | [下载PDF](https://arxiv.org/pdf/2602.04876v1.pdf)

---

## [9. LitS: A novel Neighborhood Descriptor for Point Clouds](https://arxiv.org/abs/2602.04838v1)

**作者**：Jonatan B. Bastos, Francisco F. Rivera, Oscar G. Lorenzo 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-04

### 📄 论文摘要

With the advancement of 3D scanning technologies, point clouds have become fundamental for representing 3D spatial data, with applications that span across various scientific and technological fields. Practical analysis of this data depends crucially on available neighborhood descriptors to accurately characterize the local geometries of the point cloud. This paper introduces LitS, a novel neighborhood descriptor for 2D and 3D point clouds. LitS are piecewise constant functions on the unit circle that allow points to keep track of their surroundings. Each element in LitS' domain represents a direction with respect to a local reference system. Once constructed, evaluating LitS at any given direction gives us information about the number of neighbors in a cone-like region centered around that same direction. Thus, LitS conveys a lot of information about the local neighborhood of a point, which can be leveraged to gain global structural understanding by analyzing how LitS changes between close points. In addition, LitS comes in two versions ('regular' and 'cumulative') and has two parameters, allowing them to adapt to various contexts and types of point clouds. Overall, they are a versatile neighborhood descriptor, capable of capturing the nuances of local point arrangements and resilient to common point cloud data issues such as variable density and noise.

### 🤖 AI 总结

**一句话总结**：本文提出了一种新颖的邻域描述符LitS，用于准确表征点云的局部几何特征。

**研究动机**：随着3D扫描技术的发展，点云在多个科学和技术领域中变得至关重要，分析这些数据需要有效的邻域描述符。

**核心方法**：LitS是单位圆上的分段常数函数，能够记录点的周围环境，并通过评估特定方向的信息来捕捉邻域特征。

**主要结论**：LitS是一种灵活的邻域描述符，适应多种点云类型，并能有效处理常见的数据问题，如密度变化和噪声。

**关键词**：点云, 邻域描述符, 3D扫描, 几何特征, LitS, 机器学习, 深度学习, 语义搜索, 自适应算法, 数据分析, rag

**评分**：58

**论文链接**：[查看原文](https://arxiv.org/abs/2602.04838v1) | [下载PDF](https://arxiv.org/pdf/2602.04838v1.pdf)

---

## [10. Toward Reliable and Explainable Nail Disease Classification: Leveraging Adversarial Training and Grad-CAM Visualization](https://arxiv.org/abs/2602.04820v1)

**作者**：Farzia Hossain, Samanta Ghosh, Shahida Begum 等 7 位作者  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-02-04

### 📄 论文摘要

Human nail diseases are gradually observed over all age groups, especially among older individuals, often going ignored until they become severe. Early detection and accurate diagnosis of such conditions are important because they sometimes reveal our body's health problems. But it is challenging due to the inferred visual differences between disease types. This paper presents a machine learning-based model for automated classification of nail diseases based on a publicly available dataset, which contains 3,835 images scaling six categories. In 224x224 pixels, all images were resized to ensure consistency. To evaluate performance, four well-known CNN models-InceptionV3, DenseNet201, EfficientNetV2, and ResNet50 were trained and analyzed. Among these, InceptionV3 outperformed the others with an accuracy of 95.57%, while DenseNet201 came next with 94.79%. To make the model stronger and less likely to make mistakes on tricky or noisy images, we used adversarial training. To help understand how the model makes decisions, we used SHAP to highlight important features in the predictions. This system could be a helpful support for doctors, making nail disease diagnosis more accurate and faster.

### 🤖 AI 总结

**一句话总结**：本文提出了一种基于机器学习的指甲疾病分类模型，通过对抗训练和SHAP可视化提升准确性和可解释性。

**研究动机**：人类指甲疾病在各年龄段普遍存在，早期检测与准确诊断对健康至关重要，但由于疾病类型间的视觉差异，分类任务具有挑战性。

**核心方法**：研究中使用了四种CNN模型进行训练和评估，并在此基础上采用对抗训练增强模型鲁棒性，同时利用SHAP可视化重要特征以增加模型的可解释性。

**主要结论**：InceptionV3模型在所有测试中表现最佳，准确率达到95.57%，该系统可为医生提供有效支持，提高指甲疾病的诊断效率和准确性。

**关键词**：机器学习, 深度学习, 卷积神经网络, 视觉分类, 对抗训练, Grad-CAM, 自动化诊断, 医学图像分析, 特征重要性, machine learning

**评分**：52

**论文链接**：[查看原文](https://arxiv.org/abs/2602.04820v1) | [下载PDF](https://arxiv.org/pdf/2602.04820v1.pdf)

---

## [11. XtraLight-MedMamba for Classification of Neoplastic Tubular Adenomas](https://arxiv.org/abs/2602.04819v1)

**作者**：Aqsa Sultana, Rayan Afsar, Ahmed Rahu 等 8 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-02-04

### 📄 论文摘要

Accurate risk stratification of precancerous polyps during routine colonoscopy screenings is essential for lowering the risk of developing colorectal cancer (CRC). However, assessment of low-grade dysplasia remains limited by subjective histopathologic interpretation. Advancements in digital pathology and deep learning provide new opportunities to identify subtle and fine morphologic patterns associated with malignant progression that may be imperceptible to the human eye. In this work, we propose XtraLight-MedMamba, an ultra-lightweight state-space-based deep learning framework for classifying neoplastic tubular adenomas from whole-slide images (WSIs). The architecture is a blend of ConvNext based shallow feature extractor with parallel vision mamba to efficiently model both long- and short-range dependencies and image generalization. An integration of Spatial and Channel Attention Bridge (SCAB) module enhances multiscale feature extraction, while Fixed Non-Negative Orthogonal Classifier (FNOClassifier) enables substantial parameter reduction and improved generalization. The model was evaluated on a curated dataset acquired from patients with low-grade tubular adenomas, stratified into case and control cohorts based on subsequent CRC development. XtraLight-MedMamba achieved an accuracy of 97.18% and an F1-score of 0.9767 using approximately 32,000 parameters, outperforming transformer-based and conventional Mamba architectures with significantly higher model complexity.

### 🤖 AI 总结

**一句话总结**：XtraLight-MedMamba是一种超轻量级深度学习框架，能高效分类肿瘤性管腺瘤，准确率达97.18%。

**研究动机**：在常规结肠镜筛查中，准确评估前癌性息肉的风险对于降低结直肠癌风险至关重要，但低级别异型增生的主观病理评估仍存在局限。

**核心方法**：本研究提出XtraLight-MedMamba框架，结合ConvNext浅层特征提取器与并行视觉Mamba，有效建模长短距离依赖，集成空间和通道注意力模块以增强多尺度特征提取。

**主要结论**：XtraLight-MedMamba在低级别管腺瘤数据集上的表现优于变压器和传统Mamba架构，显示出更高的准确性和更少的参数使用。

**关键词**：深度学习, 机器学习, 神经网络, 图像分类, 低级别腺瘤, 风险分层, 数字病理, 特征提取, 多尺度特征, deep learning

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.04819v1) | [下载PDF](https://arxiv.org/pdf/2602.04819v1.pdf)

---

## [12. X2HDR: HDR Image Generation in a Perceptually Uniform Space](https://arxiv.org/abs/2602.04814v1)

**作者**：Ronghuan Wu, Wanchao Su, Kede Ma 等 5 位作者  
**分类**：cs.CV, cs.GR  
**发布时间**：2026-02-04

### 📄 论文摘要

High-dynamic-range (HDR) formats and displays are becoming increasingly prevalent, yet state-of-the-art image generators (e.g., Stable Diffusion and FLUX) typically remain limited to low-dynamic-range (LDR) output due to the lack of large-scale HDR training data. In this work, we show that existing pretrained diffusion models can be easily adapted to HDR generation without retraining from scratch. A key challenge is that HDR images are natively represented in linear RGB, whose intensity and color statistics differ substantially from those of sRGB-encoded LDR images. This gap, however, can be effectively bridged by converting HDR inputs into perceptually uniform encodings (e.g., using PU21 or PQ). Empirically, we find that LDR-pretrained variational autoencoders (VAEs) reconstruct PU21-encoded HDR inputs with fidelity comparable to LDR data, whereas linear RGB inputs cause severe degradations. Motivated by this finding, we describe an efficient adaptation strategy that freezes the VAE and finetunes only the denoiser via low-rank adaptation in a perceptually uniform space. This results in a unified computational method that supports both text-to-HDR synthesis and single-image RAW-to-HDR reconstruction. Experiments demonstrate that our perceptually encoded adaptation consistently improves perceptual fidelity, text-image alignment, and effective dynamic range, relative to previous techniques.

### 🤖 AI 总结

**一句话总结**：本研究提出了一种通过感知统一空间实现HDR图像生成的新方法，能有效提高HDR生成的视觉保真度。

**研究动机**：随着HDR格式和显示屏的普及，现有图像生成模型在HDR生成上受到大规模训练数据的限制，因此需要一种有效的适应策略。

**核心方法**：通过将HDR输入转换为感知统一编码（如PU21或PQ），冻结变分自编码器（VAE），并仅微调去噪器，从而实现LDR预训练模型的HDR生成适应。

**主要结论**：实验表明，所提出的方法在感知保真度、文本与图像对齐及有效动态范围方面均优于之前的技术。

**关键词**：生成图像, 高动态范围, 预训练模型, 视觉感知, 低秩适应, 图像重建, 生成对抗网络, 变分自编码器, perceptually uniform encoding, diffusion

**评分**：60

**论文链接**：[查看原文](https://arxiv.org/abs/2602.04814v1) | [下载PDF](https://arxiv.org/pdf/2602.04814v1.pdf)

---

## [13. Light Forcing: Accelerating Autoregressive Video Diffusion via Sparse Attention](https://arxiv.org/abs/2602.04789v1)

**作者**：Chengtao Lv, Yumeng Shi, Yushi Huang 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-04

### 📄 论文摘要

Advanced autoregressive (AR) video generation models have improved visual fidelity and interactivity, but the quadratic complexity of attention remains a primary bottleneck for efficient deployment. While existing sparse attention solutions have shown promise on bidirectional models, we identify that applying these solutions to AR models leads to considerable performance degradation for two reasons: isolated consideration of chunk generation and insufficient utilization of past informative context. Motivated by these observations, we propose \textsc{Light Forcing}, the \textit{first} sparse attention solution tailored for AR video generation models. It incorporates a \textit{Chunk-Aware Growth} mechanism to quantitatively estimate the contribution of each chunk, which determines their sparsity allocation. This progressive sparsity increase strategy enables the current chunk to inherit prior knowledge in earlier chunks during generation. Additionally, we introduce a \textit{Hierarchical Sparse Attention} to capture informative historical and local context in a coarse-to-fine manner. Such two-level mask selection strategy (\ie, frame and block level) can adaptively handle diverse attention patterns. Extensive experiments demonstrate that our method outperforms existing sparse attention in quality (\eg, 84.5 on VBench) and efficiency (\eg, $1.2{\sim}1.3\times$ end-to-end speedup). Combined with FP8 quantization and LightVAE, \textsc{Light Forcing} further achieves a $2.3\times$ speedup and 19.7\,FPS on an RTX~5090 GPU. Code will be released at \href{https://github.com/chengtao-lv/LightForcing}{https://github.com/chengtao-lv/LightForcing}.

### 🤖 AI 总结

**一句话总结**：提出了一种名为Light Forcing的稀疏注意力机制，以提升自回归视频生成模型的效率和质量。

**研究动机**：现有的稀疏注意力解决方案在自回归模型中表现不佳，主要由于对生成块的孤立考虑和未充分利用过去信息的上下文。

**核心方法**：Light Forcing引入了块感知增长机制和分层稀疏注意力策略，以定量估计每块的贡献并在生成过程中继承先前的知识。

**主要结论**：实验结果表明，Light Forcing在生成质量和效率上均优于现有稀疏注意力方法，并在RTX 5090 GPU上实现了显著的速度提升。

**关键词**：稀疏注意力, 自回归视频生成, 生成模型, 机器学习, 深度学习, 神经网络, 结构化稀疏, 逐层掩码选择, 速度提升, FP8量化, diffusion

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2602.04789v1) | [下载PDF](https://arxiv.org/pdf/2602.04789v1.pdf)

---

## cs.LG

## [14. Protein Autoregressive Modeling via Multiscale Structure Generation](https://arxiv.org/abs/2602.04883v1)

**作者**：Yanru Qu, Cheng-Yen Hsieh, Zaixiang Zheng 等 5 位作者  
**分类**：cs.LG, cs.AI, q-bio.BM, q-bio.QM  
**发布时间**：2026-02-04

### 📄 论文摘要

We present protein autoregressive modeling (PAR), the first multi-scale autoregressive framework for protein backbone generation via coarse-to-fine next-scale prediction. Using the hierarchical nature of proteins, PAR generates structures that mimic sculpting a statue, forming a coarse topology and refining structural details over scales. To achieve this, PAR consists of three key components: (i) multi-scale downsampling operations that represent protein structures across multiple scales during training; (ii) an autoregressive transformer that encodes multi-scale information and produces conditional embeddings to guide structure generation; (iii) a flow-based backbone decoder that generates backbone atoms conditioned on these embeddings. Moreover, autoregressive models suffer from exposure bias, caused by the training and the generation procedure mismatch, and substantially degrades structure generation quality. We effectively alleviate this issue by adopting noisy context learning and scheduled sampling, enabling robust backbone generation. Notably, PAR exhibits strong zero-shot generalization, supporting flexible human-prompted conditional generation and motif scaffolding without requiring fine-tuning. On the unconditional generation benchmark, PAR effectively learns protein distributions and produces backbones of high design quality, and exhibits favorable scaling behavior. Together, these properties establish PAR as a promising framework for protein structure generation.

### 🤖 AI 总结

**一句话总结**：提出了一种名为蛋白质自回归建模（PAR）的多尺度框架，用于蛋白质骨架的生成，能够有效缓解生成过程中的曝光偏差问题。

**研究动机**：蛋白质结构生成的准确性和灵活性对于生物学和药物设计至关重要，因此需要一种新的框架来提升结构生成的质量和泛化能力。

**核心方法**：PAR框架通过多尺度下采样、基于自回归的变换器和流式解码器来实现蛋白质骨架的生成，同时采用噪声上下文学习和调度采样来克服曝光偏差。

**主要结论**：PAR在无条件生成基准测试中表现出色，能够学习蛋白质分布并生成高质量的骨架，展示出强大的零-shot 泛化能力，适用于人类提示的条件生成。

**关键词**：蛋白质, 自回归模型, 多尺度, 生成, 变换器, 结构生成, 条件嵌入, 训练, 生成质量, 无监督学习, transformer

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2602.04883v1) | [下载PDF](https://arxiv.org/pdf/2602.04883v1.pdf)

---

## [15. Multi-Head LatentMoE and Head Parallel: Communication-Efficient and Deterministic MoE Parallelism](https://arxiv.org/abs/2602.04870v1)

**作者**：Chenwei Cui, Rockwell Jackson, Benjamin Joseph Herrera 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-04

### 📄 论文摘要

Large language models have transformed many applications but remain expensive to train. Sparse Mixture of Experts (MoE) addresses this through conditional computation, with Expert Parallel (EP) as the standard distributed training method. However, EP has three limitations: communication cost grows linearly with the number of activated experts $k$, load imbalance affects latency and memory usage, and data-dependent communication requires metadata exchange. We propose Multi-Head LatentMoE and Head Parallel (HP), a new architecture and parallelism achieving $O(1)$ communication cost regardless of $k$, completely balanced traffic, and deterministic communication, all while remaining compatible with EP. To accelerate Multi-Head LatentMoE, we propose IO-aware routing and expert computation. Compared to MoE with EP, Multi-Head LatentMoE with HP trains up to $1.61\times$ faster while having identical performance. With doubled granularity, it achieves higher overall performance while still being $1.11\times$ faster. Our method makes multi-billion-parameter foundation model research more accessible.

### 🤖 AI 总结

**一句话总结**：提出了一种新架构Multi-Head LatentMoE和Head Parallel，显著降低了稀疏专家模型的通信成本和不平衡问题，同时加速训练。

**研究动机**：大型语言模型训练成本高，稀疏Mixture of Experts (MoE)通过条件计算来解决这一问题，但现有的专家并行方法存在通信成本和负载不平衡等限制。

**核心方法**：提出了Multi-Head LatentMoE和Head Parallel架构，实现了与激活专家数量无关的O(1)通信成本，采用IO感知路由和专家计算加速训练。

**主要结论**：与专家并行的MoE相比，Multi-Head LatentMoE和Head Parallel训练速度提高了1.61倍，且在性能上保持一致，使多亿参数基础模型的研究更加可及。

**关键词**：多头, LatentMoE, MoE, 专家并行, 训练加速, 稀疏混合专家, 负载均衡, 确定性通信, 语义搜索, 深度学习, agent

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.04870v1) | [下载PDF](https://arxiv.org/pdf/2602.04870v1.pdf)

---

## [16. CRoSS: A Continual Robotic Simulation Suite for Scalable Reinforcement Learning with High Task Diversity and Realistic Physics Simulation](https://arxiv.org/abs/2602.04868v1)

**作者**：Yannick Denker, Alexander Gepperth  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-04

### 📄 论文摘要

Continual reinforcement learning (CRL) requires agents to learn from a sequence of tasks without forgetting previously acquired policies. In this work, we introduce a novel benchmark suite for CRL based on realistically simulated robots in the Gazebo simulator. Our Continual Robotic Simulation Suite (CRoSS) benchmarks rely on two robotic platforms: a two-wheeled differential-drive robot with lidar, camera and bumper sensor, and a robotic arm with seven joints. The former represent an agent in line-following and object-pushing scenarios, where variation of visual and structural parameters yields a large number of distinct tasks, whereas the latter is used in two goal-reaching scenarios with high-level cartesian hand position control (modeled after the Continual World benchmark), and low-level control based on joint angles. For the robotic arm benchmarks, we provide additional kinematics-only variants that bypass the need for physical simulation (as long as no sensor readings are required), and which can be run two orders of magnitude faster. CRoSS is designed to be easily extensible and enables controlled studies of continual reinforcement learning in robotic settings with high physical realism, and in particular allow the use of almost arbitrary simulated sensors. To ensure reproducibility and ease of use, we provide a containerized setup (Apptainer) that runs out-of-the-box, and report performances of standard RL algorithms, including Deep Q-Networks (DQN) and policy gradient methods. This highlights the suitability as a scalable and reproducible benchmark for CRL research.

### 🤖 AI 总结

**一句话总结**：CRoSS是一个新颖的持续强化学习基准套件，专为多任务和真实物理模拟的机器人而设计。

**研究动机**：持续强化学习需要智能体在学习新任务的同时保持对已学策略的记忆，因此需要一个高任务多样性和真实物理模拟的基准。

**核心方法**：CRoSS基于Gazebo模拟器，利用两种机器人平台（差动驱动机器人和七关节机械臂）进行多种任务的评估，并提供了易于扩展的容器化设置以确保可复现性。

**主要结论**：CRoSS作为一个可扩展且可复现的基准，适合用于机器人领域的持续强化学习研究，支持多种传感器的使用。

**关键词**：持续学习, 强化学习, 机器人模拟, 任务多样性, Gazebo, 代理, 深度学习, 控制算法, kinematics, 物理仿真, agent

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.04868v1) | [下载PDF](https://arxiv.org/pdf/2602.04868v1.pdf)

---

## [17. Subliminal Effects in Your Data: A General Mechanism via Log-Linearity](https://arxiv.org/abs/2602.04863v1)

**作者**：Ishaq Aden-Ali, Noah Golowich, Allen Liu 等 6 位作者  
**分类**：cs.LG, cs.AI, cs.CL, stat.ML  
**发布时间**：2026-02-04

### 📄 论文摘要

Training modern large language models (LLMs) has become a veritable smorgasbord of algorithms and datasets designed to elicit particular behaviors, making it critical to develop techniques to understand the effects of datasets on the model's properties. This is exacerbated by recent experiments that show datasets can transmit signals that are not directly observable from individual datapoints, posing a conceptual challenge for dataset-centric understandings of LLM training and suggesting a missing fundamental account of such phenomena. Towards understanding such effects, inspired by recent work on the linear structure of LLMs, we uncover a general mechanism through which hidden subtexts can arise in generic datasets.   We introduce Logit-Linear-Selection (LLS), a method that prescribes how to select subsets of a generic preference dataset to elicit a wide range of hidden effects. We apply LLS to discover subsets of real-world datasets so that models trained on them exhibit behaviors ranging from having specific preferences, to responding to prompts in a different language not present in the dataset, to taking on a different persona. Crucially, the effect persists for the selected subset, across models with varying architectures, supporting its generality and universality.

### 🤖 AI 总结

**一句话总结**：该论文提出了一种通过Logit-Linear-Selection方法揭示数据集中隐含的潜在效应的机制，进而影响大型语言模型的行为。

**研究动机**：随着大型语言模型（LLM）训练的复杂性增加，理解数据集对模型属性的影响变得至关重要，尤其是在数据集传递不可直接观察信号的情况下。

**核心方法**：引入Logit-Linear-Selection（LLS）方法，以选择通用偏好数据集的子集，从而发现数据集中潜在的隐含效应。

**主要结论**：所提出的方法在不同模型架构上均能保持其效果，证明了其普遍性和广泛适用性。

**关键词**：潜在效应, 数据集, 大语言模型, LLM, Logit-Linear-Selection, 隐藏效果, 训练方法, 模型行为, 数据选择, 语言响应

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.04863v1) | [下载PDF](https://arxiv.org/pdf/2602.04863v1.pdf)

---

## [18. From Evaluation to Design: Using Potential Energy Surface Smoothness Metrics to Guide Machine Learning Interatomic Potential Architectures](https://arxiv.org/abs/2602.04861v1)

**作者**：Ryan Liu, Eric Qu, Tobias Kreiman 等 5 位作者  
**分类**：cs.LG, cond-mat.mtrl-sci, cs.AI, physics.chem-ph  
**发布时间**：2026-02-04

### 📄 论文摘要

Machine Learning Interatomic Potentials (MLIPs) sometimes fail to reproduce the physical smoothness of the quantum potential energy surface (PES), leading to erroneous behavior in downstream simulations that standard energy and force regression evaluations can miss. Existing evaluations, such as microcanonical molecular dynamics (MD), are computationally expensive and primarily probe near-equilibrium states. To improve evaluation metrics for MLIPs, we introduce the Bond Smoothness Characterization Test (BSCT). This efficient benchmark probes the PES via controlled bond deformations and detects non-smoothness, including discontinuities, artificial minima, and spurious forces, both near and far from equilibrium. We show that BSCT correlates strongly with MD stability while requiring a fraction of the cost of MD. To demonstrate how BSCT can guide iterative model design, we utilize an unconstrained Transformer backbone as a testbed, illustrating how refinements such as a new differentiable $k$-nearest neighbors algorithm and temperature-controlled attention reduce artifacts identified by our metric. By optimizing model design systematically based on BSCT, the resulting MLIP simultaneously achieves a low conventional E/F regression error, stable MD simulations, and robust atomistic property predictions. Our results establish BSCT as both a validation metric and as an "in-the-loop" model design proxy that alerts MLIP developers to physical challenges that cannot be efficiently evaluated by current MLIP benchmarks.

### 🤖 AI 总结

**一句话总结**：论文提出了一种新的评估指标BSCT，旨在通过检测量子势能面光滑性来指导机器学习原子间势的设计与优化。

**研究动机**：现有的机器学习原子间势评估方法效率低且主要集中在平衡态，导致无法有效捕捉潜在的物理问题。

**核心方法**：提出的BSCT通过控制键变形来探测势能面光滑性，能够有效识别不连续性、人工极小值和虚假力，同时成本远低于传统的分子动力学模拟。

**主要结论**：通过基于BSCT的系统优化，所设计的机器学习模型不仅降低了传统的能量/力回归误差，还实现了稳定的分子动力学模拟和可靠的原子性质预测，证明了BSCT在模型设计中的重要性。

**关键词**：机器学习, 量子势能面, 深度学习, 变换器, 模型设计, 迭代优化, 分子动力学, 平滑性评估, 物理挑战, machine learning

**评分**：68

**论文链接**：[查看原文](https://arxiv.org/abs/2602.04861v1) | [下载PDF](https://arxiv.org/pdf/2602.04861v1.pdf)

---

## [19. The Key to State Reduction in Linear Attention: A Rank-based Perspective](https://arxiv.org/abs/2602.04852v1)

**作者**：Philipp Nazari, T. Konstantin Rusch  
**分类**：cs.LG  
**发布时间**：2026-02-04

### 📄 论文摘要

Linear attention offers a computationally efficient yet expressive alternative to softmax attention. However, recent empirical results indicate that the state of trained linear attention models often exhibits a low-rank structure, suggesting that these models underexploit their capacity in practice. To illuminate this phenomenon, we provide a theoretical analysis of the role of rank in linear attention, revealing that low effective rank can affect retrieval error by amplifying query noise. In addition to these theoretical insights, we conjecture that the low-rank states can be substantially reduced post-training with only minimal performance degradation, yielding faster and more memory-efficient models. To this end, we propose a novel hardware-aware approach that structurally prunes key and query matrices, reducing the state size while retaining compatibility with existing CUDA kernels. We adapt several existing pruning strategies to fit our framework and, building on our theoretical analysis, propose a novel structured pruning method based on a rank-revealing QR decomposition. Our empirical results, evaluated across models of varying sizes and on various downstream tasks, demonstrate the effectiveness of our state reduction framework. We highlight that our framework enables the removal of 50% of the query and key channels at only a marginal increase in perplexity. The code for this project can be found at https://github.com/camail-official/LinearAttentionPruning.

### 🤖 AI 总结

**一句话总结**：本文提出了一种基于秩的线性注意力状态简化方法，通过结构性修剪和理论分析，显著减少模型状态大小，同时保持性能。

**研究动机**：线性注意力模型的训练状态常表现出低秩结构，表明其未充分利用模型容量，导致检索错误增加。

**核心方法**：提出了一种新颖的硬件感知方法，通过结构性修剪关键和查询矩阵，结合基于秩揭示QR分解的结构化修剪策略。

**主要结论**：实验结果表明，该框架能够在仅轻微增加困惑度的情况下，去除50%的查询和关键通道，提升模型效率。

**关键词**：线性注意力, 低秩结构, 检索误差, 硬件感知, 结构化剪枝, CUDA, QR分解, 模型压缩, 性能优化, retrieval

**评分**：60

**论文链接**：[查看原文](https://arxiv.org/abs/2602.04852v1) | [下载PDF](https://arxiv.org/pdf/2602.04852v1.pdf)

---

## [20. Safe Urban Traffic Control via Uncertainty-Aware Conformal Prediction and World-Model Reinforcement Learning](https://arxiv.org/abs/2602.04821v1)

**作者**：Joydeep Chandra, Satyam Kumar Navneet, Aleksandr Algazinov 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-04

### 📄 论文摘要

Urban traffic management demands systems that simultaneously predict future conditions, detect anomalies, and take safe corrective actions -- all while providing reliability guarantees. We present STREAM-RL, a unified framework that introduces three novel algorithmic contributions: (1) PU-GAT+, an Uncertainty-Guided Adaptive Conformal Forecaster that uses prediction uncertainty to dynamically reweight graph attention via confidence-monotonic attention, achieving distribution-free coverage guarantees; (2) CRFN-BY, a Conformal Residual Flow Network that models uncertainty-normalized residuals via normalizing flows with Benjamini-Yekutieli FDR control under arbitrary dependence; and (3) LyCon-WRL+, an Uncertainty-Guided Safe World-Model RL agent with Lyapunov stability certificates, certified Lipschitz bounds, and uncertainty-propagated imagination rollouts. To our knowledge, this is the first framework to propagate calibrated uncertainty from forecasting through anomaly detection to safe policy learning with end-to-end theoretical guarantees. Experiments on multiple real-world traffic trajectory data demonstrate that STREAM-RL achieves 91.4\% coverage efficiency, controls FDR at 4.1\% under verified dependence, and improves safety rate to 95.2\% compared to 69\% for standard PPO while achieving higher reward, with 23ms end-to-end inference latency.

### 🤖 AI 总结

**一句话总结**：本文提出了一种名为STREAM-RL的城市交通控制框架，利用不确定性感知的预测和强化学习提高交通管理的安全性和效率。

**研究动机**：城市交通管理需要能够预测未来状况、检测异常并采取安全措施的系统，同时提供可靠性保证。

**核心方法**：STREAM-RL框架结合了三种新算法，分别是基于不确定性的自适应符合预测、符合残差流网络和不确定性引导的安全世界模型强化学习代理。

**主要结论**：实验结果表明，STREAM-RL在覆盖效率、安全率和奖励上均优于传统方法，展示了其在真实交通数据中的有效性。

**关键词**：城市交通管理, 不确定性预测, 强化学习, 流网络, 安全控制, 预测不确定性, 自适应模型, anomaly detection, STREAM-RL, agent

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.04821v1) | [下载PDF](https://arxiv.org/pdf/2602.04821v1.pdf)

---

## [21. Beyond Rewards in Reinforcement Learning for Cyber Defence](https://arxiv.org/abs/2602.04809v1)

**作者**：Elizabeth Bates, Chris Hicks, Vasilios Mavroudis  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-04

### 📄 论文摘要

Recent years have seen an explosion of interest in autonomous cyber defence agents trained to defend computer networks using deep reinforcement learning. These agents are typically trained in cyber gym environments using dense, highly engineered reward functions which combine many penalties and incentives for a range of (un)desirable states and costly actions. Dense rewards help alleviate the challenge of exploring complex environments but risk biasing agents towards suboptimal and potentially riskier solutions, a critical issue in complex cyber environments. We thoroughly evaluate the impact of reward function structure on learning and policy behavioural characteristics using a variety of sparse and dense reward functions, two well-established cyber gyms, a range of network sizes, and both policy gradient and value-based RL algorithms. Our evaluation is enabled by a novel ground truth evaluation approach which allows directly comparing between different reward functions, illuminating the nuanced inter-relationships between rewards, action space and the risks of suboptimal policies in cyber environments. Our results show that sparse rewards, provided they are goal aligned and can be encountered frequently, uniquely offer both enhanced training reliability and more effective cyber defence agents with lower-risk policies. Surprisingly, sparse rewards can also yield policies that are better aligned with cyber defender goals and make sparing use of costly defensive actions without explicit reward-based numerical penalties.

### 🤖 AI 总结

**一句话总结**：本文探讨了稀疏奖励在网络防御中的应用，表明其比密集奖励更能有效训练安全代理并降低风险。

**研究动机**：随着自动化网络防御代理的兴起，研究如何优化奖励函数以提升安全性和有效性变得尤为重要。

**核心方法**：通过对不同奖励函数的结构进行评估，结合多种网络环境和RL算法，使用创新的真实性评估方法进行比较。

**主要结论**：稀疏奖励在目标对齐和频繁遭遇的情况下，不仅提高了训练的可靠性，还能够生成更符合网络防御目标的低风险策略。

**关键词**：深度学习, 强化学习, 自主代理, 网络防御, 奖励函数, 稀疏奖励, 政策梯度, 行为特征, 网络安全, 复杂环境, agent

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.04809v1) | [下载PDF](https://arxiv.org/pdf/2602.04809v1.pdf)

---

## [22. Evolving Afferent Architectures: Biologically-inspired Models for Damage-Avoidance Learning](https://arxiv.org/abs/2602.04807v1)

**作者**：Wolfgang Maass, Sabine Janzen, Prajvi Saxena 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-04

### 📄 论文摘要

We introduce Afferent Learning, a framework that produces Computational Afferent Traces (CATs) as adaptive, internal risk signals for damage-avoidance learning. Inspired by biological systems, the framework uses a two-level architecture: evolutionary optimization (outer loop) discovers afferent sensing architectures that enable effective policy learning, while reinforcement learning (inner loop) trains damage-avoidance policies using these signals. This formalizes afferent sensing as providing an inductive bias for efficient learning: architectures are selected based on their ability to enable effective learning (rather than directly minimizing damage). We provide theoretical convergence guarantees under smoothness and bounded-noise assumptions. We illustrate the general approach in the challenging context of biomechanical digital twins operating over long time horizons (multiple decades of the life-course). Here, we find that CAT-based evolved architectures achieve significantly higher efficiency and better age-robustness than hand-designed baselines, enabling policies that exhibit age-dependent behavioral adaptation (23% reduction in high-risk actions). Ablation studies validate CAT signals, evolution, and predictive discrepancy as essential. We release code and data for reproducibility.

### 🤖 AI 总结

**一句话总结**：本论文提出了一种生物启发的Afferent学习框架，通过适应性内部风险信号促进损伤避免学习。

**研究动机**：研究旨在通过生物系统的启发，提升损伤避免学习的效率和适应性。

**核心方法**：该框架采用两级架构，外层通过进化优化发现有效的感知架构，内层使用强化学习训练损伤避免策略。

**主要结论**：CAT基于进化的架构在效率和年龄鲁棒性上显著优于手工设计的基线，且能够实现年龄依赖的行为适应。

**关键词**：生物启发模型, 适应性, 风险信号, 强化学习, 进化优化, 计算性传入轨迹, 政策学习, 生物机械数字双胞胎, age-robustness, damage-avoidance, context

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2602.04807v1) | [下载PDF](https://arxiv.org/pdf/2602.04807v1.pdf)

---

## [23. Maximum-Volume Nonnegative Matrix Factorization](https://arxiv.org/abs/2602.04795v1)

**作者**：Olivier Vu Thanh, Nicolas Gillis  
**分类**：cs.LG, eess.SP, math.NA, stat.ML  
**发布时间**：2026-02-04

### 📄 论文摘要

Nonnegative matrix factorization (NMF) is a popular data embedding technique. Given a nonnegative data matrix $X$, it aims at finding two lower dimensional matrices, $W$ and $H$, such that $X\approx WH$, where the factors $W$ and $H$ are constrained to be element-wise nonnegative. The factor $W$ serves as a basis for the columns of $X$. In order to obtain more interpretable and unique solutions, minimum-volume NMF (MinVol NMF) minimizes the volume of $W$. In this paper, we consider the dual approach, where the volume of $H$ is maximized instead; this is referred to as maximum-volume NMF (MaxVol NMF). MaxVol NMF is identifiable under the same conditions as MinVol NMF in the noiseless case, but it behaves rather differently in the presence of noise. In practice, MaxVol NMF is much more effective to extract a sparse decomposition and does not generate rank-deficient solutions. In fact, we prove that the solutions of MaxVol NMF with the largest volume correspond to clustering the columns of $X$ in disjoint clusters, while the solutions of MinVol NMF with smallest volume are rank deficient. We propose two algorithms to solve MaxVol NMF. We also present a normalized variant of MaxVol NMF that exhibits better performance than MinVol NMF and MaxVol NMF, and can be interpreted as a continuum between standard NMF and orthogonal NMF. We illustrate our results in the context of hyperspectral unmixing.

### 🤖 AI 总结

**一句话总结**：本文提出了一种新的非负矩阵分解方法——最大体积非负矩阵分解（MaxVol NMF），通过最大化矩阵H的体积来提高稀疏分解的效果。

**研究动机**：传统的最小体积非负矩阵分解（MinVol NMF）在噪声环境下表现不佳，因此需要探索新的方法以提供更稳定和可解释的解决方案。

**核心方法**：提出了MaxVol NMF方法，旨在最大化矩阵H的体积，并且证明了其在无噪声条件下的可识别性，同时提供了两种求解算法及其归一化变体。

**主要结论**：MaxVol NMF在提取稀疏分解方面更有效，并且与MinVol NMF相比，其解决方案对应于将数据列聚类为不相交的簇，避免了秩缺陷。

**关键词**：非负矩阵分解, 数据嵌入, 机器学习, 稀疏分解, 聚类, MaxVol NMF, 最小体积 NMF, 噪声处理, 超光谱解混合, embedding

**评分**：60

**论文链接**：[查看原文](https://arxiv.org/abs/2602.04795v1) | [下载PDF](https://arxiv.org/pdf/2602.04795v1.pdf)

---

## [24. Team, Then Trim: An Assembly-Line LLM Framework for High-Quality Tabular Data Generation](https://arxiv.org/abs/2602.04785v1)

**作者**：Congjing Zhang, Ryan Feng Lin, Ruoxuan Bao 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-04

### 📄 论文摘要

While tabular data is fundamental to many real-world machine learning (ML) applications, acquiring high-quality tabular data is usually labor-intensive and expensive. Limited by the scarcity of observations, tabular datasets often exhibit critical deficiencies, such as class imbalance, selection bias, and low fidelity. To address these challenges, building on recent advances in Large Language Models (LLMs), this paper introduces Team-then-Trim (T$^2$), a framework that synthesizes high-quality tabular data through a collaborative team of LLMs, followed by a rigorous three-stage plug-in data quality control (QC) pipeline. In T$^2$, tabular data generation is conceptualized as a manufacturing process: specialized LLMs, guided by domain knowledge, are tasked with generating different data components sequentially, and the resulting products, i.e., the synthetic data, are systematically evaluated across multiple dimensions of QC. Empirical results on both simulated and real-world datasets demonstrate that T$^2$ outperforms state-of-the-art methods in producing high-quality tabular data, highlighting its potential to support downstream models when direct data collection is practically infeasible.

### 🤖 AI 总结

**一句话总结**：本文提出了一种名为Team-then-Trim (T$^2$) 的框架，通过协作的LLM团队和严格的数据质量控制流程合成高质量的表格数据。

**研究动机**：高质量的表格数据获取通常劳动密集且成本高，现有数据集存在严重不足，迫切需要有效的生成方法。

**核心方法**：T$^2$框架将表格数据生成视为制造过程，通过专业化的LLM团队依照领域知识逐步生成数据组件，并在多个维度上进行质量评估。

**主要结论**：实证结果表明，T$^2$在生成高质量表格数据方面优于现有最先进的方法，展示了其在实际应用中的潜力。

**关键词**：生成框架, 表格数据, 大规模语言模型, 数据质量控制, 协同生成, 多阶段评估, 机器学习应用, 合作团队, machine learning

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.04785v1) | [下载PDF](https://arxiv.org/pdf/2602.04785v1.pdf)

---

## [25. Dynamical Regimes of Multimodal Diffusion Models](https://arxiv.org/abs/2602.04780v1)

**作者**：Emil Albrychiewicz, Andrés Franco Valiente, Li-Ching Chen  
**分类**：cs.LG  
**发布时间**：2026-02-04

### 📄 论文摘要

Diffusion based generative models have achieved unprecedented fidelity in synthesizing high dimensional data, yet the theoretical mechanisms governing multimodal generation remain poorly understood. Here, we present a theoretical framework for coupled diffusion models, using coupled Ornstein-Uhlenbeck processes as a tractable model. By using the nonequilibrium statistical physics of dynamical phase transitions, we demonstrate that multimodal generation is governed by a spectral hierarchy of interaction timescales rather than simultaneous resolution. A key prediction is the ``synchronization gap'', a temporal window during the reverse generative process where distinct eigenmodes stabilize at different rates, providing a theoretical explanation for common desynchronization artifacts. We derive analytical conditions for speciation and collapse times under both symmetric and anisotropic coupling regimes, establishing strict bounds for coupling strength to avoid unstable symmetry breaking. We show that the coupling strength acts as a spectral filter that enforces a tunable temporal hierarchy on generation. We support these predictions through controlled experiments with diffusion models trained on MNIST datasets and exact score samplers. These results motivate time dependent coupling schedules that target mode specific timescales, offering a potential alternative to ad hoc guidance tuning.

### 🤖 AI 总结

**一句话总结**：本文提出了一个理论框架，揭示了多模态扩散模型生成的动态机制，特别是通过耦合的Ornstein-Uhlenbeck过程分析了交互时间尺度的谱层次结构。

**研究动机**：尽管扩散生成模型在合成高维数据方面取得了显著成功，但多模态生成的理论机制仍不清楚，因此需要深入研究其背后的动态规律。

**核心方法**：通过研究耦合的Ornstein-Uhlenbeck过程，利用非平衡统计物理学中的动态相变理论，分析不同时间尺度下的相互作用，并推导出相应的分析条件。

**主要结论**：研究结果表明，耦合强度作为谱滤波器，能够在生成过程中强制执行可调的时间层次，这为多模态生成提供了新的时间依赖耦合调度策略。

**关键词**：多模态, 扩散模型, 生成模型, 深度学习, 神经网络, 交互时间尺度, 同步间隙, 统计物理, 训练实验, MNIST, generative

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.04780v1) | [下载PDF](https://arxiv.org/pdf/2602.04780v1.pdf)

---

## [26. Interval-Based AUC (iAUC): Extending ROC Analysis to Uncertainty-Aware Classification](https://arxiv.org/abs/2602.04775v1)

**作者**：Yuqi Li, Matthew M. Engelhard  
**分类**：cs.LG  
**发布时间**：2026-02-04

### 📄 论文摘要

In high-stakes risk prediction, quantifying uncertainty through interval-valued predictions is essential for reliable decision-making. However, standard evaluation tools like the receiver operating characteristic (ROC) curve and the area under the curve (AUC) are designed for point scores and fail to capture the impact of predictive uncertainty on ranking performance. We propose an uncertainty-aware ROC framework specifically for interval-valued predictions, introducing two new measures: $AUC_L$ and $AUC_U$. This framework enables an informative three-region decomposition of the ROC plane, partitioning pairwise rankings into correct, incorrect, and uncertain orderings. This approach naturally supports selective prediction by allowing models to abstain from ranking cases with overlapping intervals, thereby optimizing the trade-off between abstention rate and discriminative reliability. We prove that under valid class-conditional coverage, $AUC_L$ and $AUC_U$ provide formal lower and upper bounds on the theoretical optimal AUC ($AUC^*$), characterizing the physical limit of achievable discrimination. The proposed framework applies broadly to interval-valued prediction models, regardless of the interval construction method. Experiments on real-world benchmark datasets, using bootstrap-based intervals as one instantiation, validate the framework's correctness and demonstrate its practical utility for uncertainty-aware evaluation and decision-making.

### 🤖 AI 总结

**一句话总结**：提出了一种针对区间值预测的不确定性感知ROC框架，并引入了新的评估指标AUC_L和AUC_U，以优化决策过程中的不确定性处理。

**研究动机**：在高风险预测中，通过区间值预测量化不确定性对于可靠决策至关重要，现有的AUC工具无法有效捕捉这种不确定性对排名性能的影响。

**核心方法**：提出了一种新的不确定性感知ROC框架，包含对ROC平面的三区域分解，并引入两个新指标AUC_L和AUC_U，以支持选择性预测和优化不确定性处理。

**主要结论**：实验验证了所提框架的正确性和实用性，展示了其在不确定性感知评估和决策中的有效应用。

**关键词**：不确定性分类, 预测模型, ROC曲线, AUC, interval-valued predictions, 选择性预测, 排序性能, 可靠性优化, 实验验证, 决策支持, rag

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.04775v1) | [下载PDF](https://arxiv.org/pdf/2602.04775v1.pdf)

---

## [27. Generative Modeling via Drifting](https://arxiv.org/abs/2602.04770v1)

**作者**：Mingyang Deng, He Li, Tianhong Li 等 5 位作者  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-02-04

### 📄 论文摘要

Generative modeling can be formulated as learning a mapping f such that its pushforward distribution matches the data distribution. The pushforward behavior can be carried out iteratively at inference time, for example in diffusion and flow-based models. In this paper, we propose a new paradigm called Drifting Models, which evolve the pushforward distribution during training and naturally admit one-step inference. We introduce a drifting field that governs the sample movement and achieves equilibrium when the distributions match. This leads to a training objective that allows the neural network optimizer to evolve the distribution. In experiments, our one-step generator achieves state-of-the-art results on ImageNet at 256 x 256 resolution, with an FID of 1.54 in latent space and 1.61 in pixel space. We hope that our work opens up new opportunities for high-quality one-step generation.

### 🤖 AI 总结

**一句话总结**：该论文提出了一种新的生成建模方法，即漂移模型，通过训练中演化推前分布实现高质量的一步生成。

**研究动机**：当前生成模型在推前分布匹配数据分布时存在效率和质量的挑战，因此需要一种新方法来改进这一过程。

**核心方法**：作者提出了一个漂移场，通过控制样本移动来演化推前分布，并在训练中实现分布的平衡，从而优化生成过程。

**主要结论**：实验表明，提出的一步生成器在ImageNet数据集上实现了最先进的结果，开启了高质量一步生成的新机会。

**关键词**：生成模型, 深度学习, 神经网络, 生成, 漂移模型, 训练目标, 一步推理, 图像生成, ImageNet, neural network

**评分**：67

**论文链接**：[查看原文](https://arxiv.org/abs/2602.04770v1) | [下载PDF](https://arxiv.org/pdf/2602.04770v1.pdf)

---

## [28. Billion-Scale Graph Foundation Models](https://arxiv.org/abs/2602.04768v1)

**作者**：Maya Bechler-Speicher, Yoel Gottlieb, Andrey Isakov 等 8 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-04

### 📄 论文摘要

Graph-structured data underpins many critical applications. While foundation models have transformed language and vision via large-scale pretraining and lightweight adaptation, extending this paradigm to general, real-world graphs is challenging. In this work, we present Graph Billion- Foundation-Fusion (GraphBFF): the first end-to-end recipe for building billion-parameter Graph Foundation Models (GFMs) for arbitrary heterogeneous, billion-scale graphs. Central to the recipe is the GraphBFF Transformer, a flexible and scalable architecture designed for practical billion-scale GFMs. Using the GraphBFF, we present the first neural scaling laws for general graphs and show that loss decreases predictably as either model capacity or training data scales, depending on which factor is the bottleneck. The GraphBFF framework provides concrete methodologies for data batching, pretraining, and fine-tuning for building GFMs at scale. We demonstrate the effectiveness of the framework with an evaluation of a 1.4 billion-parameter GraphBFF Transformer pretrained on one billion samples. Across ten diverse, real-world downstream tasks on graphs unseen during training, spanning node- and link-level classification and regression, GraphBFF achieves remarkable zero-shot and probing performance, including in few-shot settings, with large margins of up to 31 PRAUC points. Finally, we discuss key challenges and open opportunities for making GFMs a practical and principled foundation for graph learning at industrial scale.

### 🤖 AI 总结

**一句话总结**：本文提出了GraphBFF，这是一个用于构建十亿参数规模图基础模型的端到端框架，能够有效处理异构大规模图数据。

**研究动机**：随着图结构数据在多个关键应用中的重要性不断提升，如何将大型预训练模型的成功经验扩展到图数据上成为一项重大挑战。

**核心方法**：GraphBFF框架结合了GraphBFF Transformer架构，提供了预训练和微调的具体方法论，能够处理十亿规模的图数据。

**主要结论**：GraphBFF在多个真实世界的下游任务中展现出卓越的零-shot和少-shot性能，表明该框架为图学习提供了实用的基础模型构建方案。

**关键词**：图神经网络, 生成模型, 预训练, 微调, Transformer, 图数据, 大规模模型, 任务评估, 零样本学习

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2602.04768v1) | [下载PDF](https://arxiv.org/pdf/2602.04768v1.pdf)

---

## [29. Active Asymmetric Multi-Agent Multimodal Learning under Uncertainty](https://arxiv.org/abs/2602.04763v1)

**作者**：Rui Liu, Pratap Tokekar, Ming Lin  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-04

### 📄 论文摘要

Multi-agent systems are increasingly equipped with heterogeneous multimodal sensors, enabling richer perception but introducing modality-specific and agent-dependent uncertainty. Existing multi-agent collaboration frameworks typically reason at the agent level, assume homogeneous sensing, and handle uncertainty implicitly, limiting robustness under sensor corruption. We propose Active Asymmetric Multi-Agent Multimodal Learning under Uncertainty (A2MAML), a principled approach for uncertainty-aware, modality-level collaboration. A2MAML models each modality-specific feature as a stochastic estimate with uncertainty prediction, actively selects reliable agent-modality pairs, and aggregates information via Bayesian inverse-variance weighting. This formulation enables fine-grained, modality-level fusion, supports asymmetric modality availability, and provides a principled mechanism to suppress corrupted or noisy modalities. Extensive experiments on connected autonomous driving scenarios for collaborative accident detection demonstrate that A2MAML consistently outperforms both single-agent and collaborative baselines, achieving up to 18.7% higher accident detection rate.

### 🤖 AI 总结

**一句话总结**：提出了一种新方法A2MAML，旨在处理多智能体系统中的不确定性，优化多模态合作。

**研究动机**：随着多智能体系统普及，异构多模态传感器带来了感知能力的提升，但也引入了特定模态和代理相关的不确定性，限制了系统在传感器损坏情况下的鲁棒性。

**核心方法**：A2MAML通过将每个模态特征建模为带有不确定性预测的随机估计，主动选择可靠的代理-模态对，并通过贝叶斯逆方差加权聚合信息，实现细粒度的模态级融合。

**主要结论**：在协作事故检测的实验中，A2MAML在事故检测率上比单代理和合作基线高出最多18.7%。

**关键词**：多智能体, 多模态学习, 不确定性, 协同工作, 模态融合, agent, Bayesian, 事故检测, 自动驾驶

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.04763v1) | [下载PDF](https://arxiv.org/pdf/2602.04763v1.pdf)

---

## [30. A Dual-TransUNet Deep Learning Framework for Multi-Source Precipitation Merging and Improving Seasonal and Extreme Estimates](https://arxiv.org/abs/2602.04757v1)

**作者**：Yuchen Ye, Zixuan Qi, Shixuan Li 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-04

### 📄 论文摘要

Multi-source precipitation products (MSPs) from satellite retrievals and reanalysis are widely used for hydroclimatic monitoring, yet spatially heterogeneous biases and limited skill for extremes still constrain their hydrologic utility. Here we develop a dual-stage TransUNet-based multi-source precipitation merging framework (DDL-MSPMF) that integrates six MSPs with four ERA5 near-surface physical predictors. A first-stage classifier estimates daily precipitation occurrence probability, and a second-stage regressor fuses the classifier outputs together with all predictors to estimate daily precipitation amount at 0.25 degree resolution over China for 2001-2020. Benchmarking against multiple deep learning and hybrid baselines shows that the TransUNet - TransUNet configuration yields the best seasonal performance (R = 0.75; RMSE = 2.70 mm/day) and improves robustness relative to a single-regressor setting. For heavy precipitation (>25 mm/day), DDL-MSPMF increases equitable threat scores across most regions of eastern China and better reproduces the spatial pattern of the July 2021 Zhengzhou rainstorm, indicating enhanced extreme-event detection beyond seasonal-mean corrections. Independent evaluation over the Qinghai-Tibet Plateau using TPHiPr further supports its applicability in data-scarce regions. SHAP analysis highlights the importance of precipitation occurrence probabilities and surface pressure, providing physically interpretable diagnostics. The proposed framework offers a scalable and explainable approach for precipitation fusion and extreme-event assessment.

### 🤖 AI 总结

**一句话总结**：提出了一种双阶段TransUNet框架，融合多源降水数据以提高降水估计的准确性和极端天气事件的检测能力。

**研究动机**：现有多源降水产品在空间异质性偏差和极端天气估计上存在不足，限制了其在水文气候监测中的应用。

**核心方法**：开发了一个双阶段的TransUNet模型，其中第一阶段通过分类器估计降水发生概率，第二阶段通过回归器结合多种物理预测因子估计降水量。

**主要结论**：该框架在季节性表现和极端降水事件检测上优于传统模型，且在数据稀缺区域显示出良好的适用性。

**关键词**：深度学习, 多源降水, TransUNet, 机器学习, 预测模型, 数据融合, 极端事件检测, 语义搜索, 人机协作, deep learning

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.04757v1) | [下载PDF](https://arxiv.org/pdf/2602.04757v1.pdf)

---

