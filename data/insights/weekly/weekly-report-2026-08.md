# Weekly Research Report | 2026-02-16 ~ 2026-02-22

> generated_at: 2026-02-28T18:01:59Z
> k_selected: 4
> embedding_model: text-embedding-3-large
> chat_model: gpt-4o-mini, gpt-5.2-2025-12-11

# 周度科技趋势研究报告（2026年2月16日至2026年2月22日）

## 一、本周摘要
本周，科技领域的主要趋势集中在编码智能体的自我改进能力、结构化执行与交互反馈的结合、生成式AI的多样化应用以及多模态对齐技术的进展。编码智能体逐渐从简单的代码生成转向更复杂的自我评估与记忆能力，推动了开发效率的提升。同时，生成式AI在设计、音频内容生成等领域的应用也在不断扩展，显示出其在创作链路中的重要性。此外，针对多模态对齐的研究表明，通过冻结编码器与对比学习投影头的结合，可以实现高效的多模态表示对齐。

## 二、趋势主题

### 1. 编码智能体进入“自我改进 + 一键后端 + 更强模型”组合期
本周，编码智能体的能力正在快速演进，逐步实现自我评估、纠错和记忆的闭环。Claude Sonnet 4.6的发布为智能体提供了更强的编程能力和长上下文处理能力，支持高达100万token的上下文窗口，极大地提升了智能体的工作效率和复杂任务的处理能力。同时，Base44后端平台的推出，使得智能体的应用开发门槛大幅降低，开发者可以通过简单的命令快速部署全栈应用。

#### 代表项目对比
- **Self Improving**：聚焦于智能体自我反思与自我批判，通过闭环机制实现持续优化。
- **Base44 Backend Platform**：提供一条命令即可部署全栈应用，简化了后端配置。
- **Sonnet 4.6**：在编程能力和长上下文推理方面实现全面升级，适用于更复杂的任务。

#### 风险与下周观察
- **Self Improving**的闭环机制在缺乏真实标注的情况下可能放大错误，需关注其实际应用中的表现。
- **Base44**的技能体系需进一步验证其扩展性与复杂API的覆盖能力。
- **Sonnet 4.6**的长上下文稳定性与成本效益需在实际工作流中进行评估。

### 2. 从“偏好”到“可执行”：以结构化执行与交互反馈提升智能体可靠性与可审计性
本周，研究者们开始关注如何将LLM的偏好预测与可执行的结构化流程结合，以提升智能体在科学工作流和硬件验证中的可靠性。多项研究表明，偏好预测虽然能够稳定反映智能体的行为，但并不总能转化为下游任务的性能差异。

#### 代表项目对比
- **When Do LLM Preferences Predict Downstream Behavior?**：探讨了偏好预测与下游性能之间的关系。
- **El Agente Gráfico**：提出了用结构化执行图替代非结构化文本编排的方法，提升科学智能体的可靠性。
- **Improving Interactive In-Context Learning from Natural Language Feedback**：通过交互式学习提升智能体的自我修正能力。

#### 风险与下周观察
- 偏好测量的一致性如何影响训练与评测决策仍需进一步研究。
- 结构化执行图的标准化实施细节是否得到验证。
- 执行感知学习在工业仿真中的应用效果需持续跟踪。

### 3. 生成式AI从“设计/构建”到“语音/音乐输出”的一体化创作链路
生成式AI的应用正在向更广泛的领域扩展，包括应用构建、品牌设计与音频内容生成。新产品如Rork Max和Lyria 3展示了生成式AI在创作过程中的潜力，强调了从生成到可编辑、可分发的完整流程。

#### 代表项目对比
- **Rork Max**：一键构建覆盖Apple全平台的应用，简化了开发流程。
- **Moda**：提供平面设计的AI助手，支持完全可编辑的内容生成。
- **Lyria 3**：通过文本或图片生成音乐，展示了生成式AI在音频领域的应用。

#### 风险与下周观察
- Rork Max的应用审核与合规风险需关注。
- Moda在品牌一致性与可编辑性之间的权衡需进一步验证。
- Lyria 3的版权归属与可商用边界仍需明确。

### 4. 冻结编码器+投影头的后验多模态对齐
本周，研究者们提出了通过冻结编码器与对比学习投影头实现多模态对齐的新方法，显示出在不显式耦合的情况下，视觉、语言与时间序列的预训练表征可以实现有效对齐。

#### 代表项目对比
- **Time Series, Vision, and Language**：探讨了三模态预训练表征的对齐方法。
- **PolyFrame**：在不微调编码器的情况下提升多语言习语消歧能力。
- **Detector-in-the-Loop Tracking**：通过闭环记忆校正提升跟踪器的稳定性。

#### 风险与下周观察
- 多模态对齐的缩放规律与模态非对称性需进行定量分析。
- 信息密度自适应采样在提升效率的同时可能影响对齐的准确性。
- 闭环记忆校正在其他任务中的迁移性与效果需持续关注。

## 三、项目榜单
本周表现突出的项目包括：
1. **Self Improving** - [链接](https://clawhub.ai/ivangdavila/self-improving)  
   通过自我反思与外部反馈实现智能体的持续优化。
2. **Rork Max** - [链接](https://www.producthunt.com/products/rork-app-for-ios?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)  
   一键构建覆盖Apple全平台的应用，简化开发流程。
3. **FairScale Solana** - [链接](https://clawhub.ai/RisheeA/fairscale-solana)  
   提供实时的信誉与风险评估能力。
4. **Base44 Backend Platform** - [链接](https://www.producthunt.com/products/base44?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)  
   一条命令即可部署全栈应用，简化后端配置。
5. **Sonnet 4.6** - [链接](https://www.producthunt.com/products/claude?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)  
   在编程与长上下文推理方面实现全面升级。

## 四、关键词趋势
本周关键词趋势如下：
- **搜索**：相关项目数量上升，显示出对搜索技术的关注。
- **记忆**：智能体的记忆能力成为研究热点，相关项目数量增加。
- **数据增强**：在生成与学习过程中，数据增强技术的应用逐渐增多。
- **持续学习**：智能体的持续学习能力受到重视，相关项目数量上升。
- **语音交互**：语音交互技术的应用与开发逐渐增多。

## 五、交叉来源观察
本周的研究与产品讨论显示出多个领域的交叉趋势，尤其是在编码智能体、生成式AI与多模态对齐技术之间的互动。例如，生成式AI的应用不仅限于内容生成，还涉及到智能体的自我学习与优化，显示出技术融合的潜力。

## 六、下周预测
展望下周，预计以下趋势将继续发展：
- **Self Improving**的闭环学习机制可能会出现更多具体应用场景，尤其是在代码审阅与内容自检方面。
- **Base44**将围绕“npx一条命令部署”与“Skills替代API”的生态增长，值得关注其对Claude Code与Cursor的进一步优化。
- **Sonnet 4.6**的长上下文窗口在实际工作流中的应用反馈与表现变化将成为关注焦点。
- **Scrapling**的自适应解析与反爬能力在长期数据采集中的稳定性与新增能力信号将被持续观察。

本周的科技趋势显示出智能体技术的快速发展与应用多样化，未来的研究与产品创新将进一步推动这一领域的进步。

## 引用索引

- [arxiv:ax-2026-02-16-1] Predicting Invoice Dilution in Supply Chain Finance with Leakage Free Two Stage XGBoost, KAN (Kolmogorov Arnold Networks), and Ensemble Models (https://arxiv.org/abs/2602.15248v1)
- [arxiv:ax-2026-02-16-10] BindCLIP: A Unified Contrastive-Generative Representation Learning Framework for Virtual Screening (https://arxiv.org/abs/2602.15236v1)
- [arxiv:ax-2026-02-16-11] Automatically Finding Reward Model Biases (https://arxiv.org/abs/2602.15222v1)
- [arxiv:ax-2026-02-16-12] MAVRL: Learning Reward Functions from Multiple Feedback Types with Amortized Variational Inference (https://arxiv.org/abs/2602.15206v1)
- [arxiv:ax-2026-02-16-13] COMPOT: Calibration-Optimized Matrix Procrustes Orthogonalization for Transformers Compression (https://arxiv.org/abs/2602.15200v1)
- [arxiv:ax-2026-02-16-14] Learning Data-Efficient and Generalizable Neural Operators via Fundamental Physics Knowledge (https://arxiv.org/abs/2602.15184v1)
- [arxiv:ax-2026-02-16-15] Refine Now, Query Fast: A Decoupled Refinement Paradigm for Implicit Neural Fields (https://arxiv.org/abs/2602.15155v2)
- [arxiv:ax-2026-02-16-2] Secure and Energy-Efficient Wireless Agentic AI Networks (https://arxiv.org/abs/2602.15212v1)
- [arxiv:ax-2026-02-16-3] Mind the (DH) Gap! A Contrast in Risky Choices Between Reasoning and Conversational LLMs (https://arxiv.org/abs/2602.15173v1)
- [arxiv:ax-2026-02-16-4] AIC CTU@AVerImaTeC: dual-retriever RAG for image-text fact checking (https://arxiv.org/abs/2602.15190v1)
- [arxiv:ax-2026-02-16-5] Time-Archival Camera Virtualization for Sports and Visual Performances (https://arxiv.org/abs/2602.15181v1)
- [arxiv:ax-2026-02-16-6] Distributional Deep Learning for Super-Resolution of 4D Flow MRI under Domain Shift (https://arxiv.org/abs/2602.15167v1)
- [arxiv:ax-2026-02-16-7] Loss Knows Best: Detecting Annotation Errors in Videos via Loss Trajectories (https://arxiv.org/abs/2602.15154v1)
- [arxiv:ax-2026-02-16-8] Size Transferability of Graph Transformers with Convolutional Positional Encodings (https://arxiv.org/abs/2602.15239v1)
- [arxiv:ax-2026-02-16-9] Closing the Distribution Gap in Adversarial Training for LLMs (https://arxiv.org/abs/2602.15238v2)
- [arxiv:ax-2026-02-17-1] Improving Interactive In-Context Learning from Natural Language Feedback (https://arxiv.org/abs/2602.16066v1)
- [arxiv:ax-2026-02-17-10] Real-time Secondary Crash Likelihood Prediction Excluding Post Primary Crash Features (https://arxiv.org/abs/2602.16739v1)
- [arxiv:ax-2026-02-17-11] Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training (https://arxiv.org/abs/2602.16065v1)
- [arxiv:ax-2026-02-17-12] Extracting and Analyzing Rail Crossing Behavior Signatures from Videos using Tensor Methods (https://arxiv.org/abs/2602.16057v2)
- [arxiv:ax-2026-02-17-13] Multi-Objective Alignment of Language Models for Personalized Psychotherapy (https://arxiv.org/abs/2602.16053v1)
- [arxiv:ax-2026-02-17-14] AI-CARE: Carbon-Aware Reporting Evaluation Metric for AI Models (https://arxiv.org/abs/2602.16042v2)
- [arxiv:ax-2026-02-17-15] MolCrystalFlow: Molecular Crystal Structure Prediction via Flow Matching (https://arxiv.org/abs/2602.16020v1)
- [arxiv:ax-2026-02-17-2] Evidence-Grounded Subspecialty Reasoning: Evaluating a Curated Clinical Intelligence Layer on the 2025 Endocrinology Board-Style Examination (https://arxiv.org/abs/2602.16050v1)
- [arxiv:ax-2026-02-17-3] How Uncertain Is the Grade? A Benchmark of Uncertainty Metrics for LLM-Based Automatic Assessment (https://arxiv.org/abs/2602.16039v1)
- [arxiv:ax-2026-02-17-4] Optimization Instability in Autonomous Agentic Workflows for Clinical Symptom Detection (https://arxiv.org/abs/2602.16037v1)
- [arxiv:ax-2026-02-17-5] Language Statistics and False Belief Reasoning: Evidence from 41 Open-Weight LMs (https://arxiv.org/abs/2602.16085v1)
- [arxiv:ax-2026-02-17-6] A Curious Class of Adpositional Multiword Expressions in Korean (https://arxiv.org/abs/2602.16023v1)
- [arxiv:ax-2026-02-17-7] MedProbCLIP: Probabilistic Adaptation of Vision-Language Foundation Model for Reliable Radiograph-Report Retrieval (https://arxiv.org/abs/2602.16019v1)
- [arxiv:ax-2026-02-17-8] Quantifying LLM Attention-Head Stability: Implications for Circuit Universality (https://arxiv.org/abs/2602.16740v1)
- [arxiv:ax-2026-02-17-9] Omni-iEEG: A Large-Scale, Comprehensive iEEG Dataset and Benchmark for Epilepsy Research (https://arxiv.org/abs/2602.16072v2)
- [arxiv:ax-2026-02-18-1] LLM4Cov: Execution-Aware Agentic Learning for High-coverage Testbench Generation (https://arxiv.org/abs/2602.16953v1)
- [arxiv:ax-2026-02-18-10] Exact Certification of Data-Poisoning Attacks Using Mixed-Integer Programming (https://arxiv.org/abs/2602.16944v1)
- [arxiv:ax-2026-02-18-2] Mind the GAP: Text Safety Does Not Transfer to Tool-Call Safety in LLM Agents (https://arxiv.org/abs/2602.16943v1)
- [arxiv:ax-2026-02-18-3] SourceBench: Can AI Answers Reference Quality Web Sources? (https://arxiv.org/abs/2602.16942v1)
- [arxiv:ax-2026-02-18-4] Eigenmood Space: Uncertainty-Aware Spectral Graph Analysis of Psychological Patterns in Classical Persian Poetry (https://arxiv.org/abs/2602.16959v1)
- [arxiv:ax-2026-02-18-5] When Semantic Overlap Is Not Enough: Cross-Lingual Euphemism Transfer Between Turkish and English (https://arxiv.org/abs/2602.16957v1)
- [arxiv:ax-2026-02-18-6] HS-3D-NeRF: 3D Surface and Hyperspectral Reconstruction From Stationary Hyperspectral Images Using Multi-Channel NeRFs (https://arxiv.org/abs/2602.16950v1)
- [arxiv:ax-2026-02-18-7] Multi-Agent Lipschitz Bandits (https://arxiv.org/abs/2602.16965v1)
- [arxiv:ax-2026-02-18-8] Neural Proposals, Symbolic Guarantees: Neuro-Symbolic Graph Generation with Hard Constraints (https://arxiv.org/abs/2602.16954v2)
- [arxiv:ax-2026-02-18-9] Beyond Message Passing: A Symbolic Alternative for Expressive and Interpretable Graph Learning (https://arxiv.org/abs/2602.16947v2)
- [arxiv:ax-2026-02-19-1] El Agente Gráfico: Structured Execution Graphs for Scientific Agents (https://arxiv.org/abs/2602.17902v1)
- [arxiv:ax-2026-02-19-10] ADAPT: Hybrid Prompt Optimization for LLM Feature Visualization (https://arxiv.org/abs/2602.17867v1)
- [arxiv:ax-2026-02-19-11] Financial time series augmentation using transformer based GAN architecture (https://arxiv.org/abs/2602.17865v1)
- [arxiv:ax-2026-02-19-12] JAX-Privacy: A library for differentially private machine learning (https://arxiv.org/abs/2602.17861v1)
- [arxiv:ax-2026-02-19-13] Neural Prior Estimation: Learning Class Priors from Latent Representations (https://arxiv.org/abs/2602.17853v1)
- [arxiv:ax-2026-02-19-14] Quad Length Codes for Lossless Compression of e4m3 (https://arxiv.org/abs/2602.17849v2)
- [arxiv:ax-2026-02-19-15] Two Calm Ends and the Wild Middle: A Geometric Picture of Memorization in Diffusion Models (https://arxiv.org/abs/2602.17846v1)
- [arxiv:ax-2026-02-19-2] Understanding Unreliability of Steering Vectors in Language Models: Geometric Predictors and the Limits of Linear Approximations (https://arxiv.org/abs/2602.17881v1)
- [arxiv:ax-2026-02-19-3] Understanding the Fine-Grained Knowledge Capabilities of Vision-Language Models (https://arxiv.org/abs/2602.17871v1)
- [arxiv:ax-2026-02-19-4] Learning Compact Video Representations for Efficient Long-form Video Understanding in Large Multimodal Models (https://arxiv.org/abs/2602.17869v1)
- [arxiv:ax-2026-02-19-5] On the Evaluation Protocol of Gesture Recognition for UAV-based Rescue Operation based on Deep Learning: A Subject-Independence Perspective (https://arxiv.org/abs/2602.17854v1)
- [arxiv:ax-2026-02-19-6] Breaking the Correlation Plateau: On the Optimization and Capacity Limits of Attention-Based Regressors (https://arxiv.org/abs/2602.17898v1)
- [arxiv:ax-2026-02-19-7] COMBA: Cross Batch Aggregation for Learning Large Graphs with Context Gating State Space Models (https://arxiv.org/abs/2602.17893v1)
- [arxiv:ax-2026-02-19-8] Machine Learning Based Prediction of Surgical Outcomes in Chronic Rhinosinusitis from Clinical Data (https://arxiv.org/abs/2602.17888v1)
- [arxiv:ax-2026-02-19-9] The Geometry of Multi-Task Grokking: Transverse Instability, Superposition, and Weight Decay Phase Structure (https://arxiv.org/abs/2602.18523v1)
- [arxiv:ax-2026-02-20-1] Decoding ML Decision: An Agentic Reasoning Framework for Large-Scale Ranking System (https://arxiv.org/abs/2602.18640v1)
- [arxiv:ax-2026-02-20-10] Adaptive Time Series Reasoning via Segment Selection (https://arxiv.org/abs/2602.18645v1)
- [arxiv:ax-2026-02-20-11] Learning Invariant Visual Representations for Planning with Joint-Embedding Predictive World Models (https://arxiv.org/abs/2602.18639v1)
- [arxiv:ax-2026-02-20-12] Online decoding of rat self-paced locomotion speed from EEG using recurrent neural networks (https://arxiv.org/abs/2602.18637v1)
- [arxiv:ax-2026-02-20-13] Non-Interfering Weight Fields: Treating Model Parameters as a Continuously Extensible Function (https://arxiv.org/abs/2602.18628v1)
- [arxiv:ax-2026-02-20-14] Diagnosing LLM Reranker Behavior Under Fixed Evidence Pools (https://arxiv.org/abs/2602.18613v1)
- [arxiv:ax-2026-02-20-15] MapTab: Can MLLMs Master Constrained Route Planning? (https://arxiv.org/abs/2602.18600v1)
- [arxiv:ax-2026-02-20-2] Feedback-based Automated Verification in Vibe Coding of CAS Adaptation Built on Constraint Logic (https://arxiv.org/abs/2602.18607v1)
- [arxiv:ax-2026-02-20-3] PolyFrame at MWE-2026 AdMIRe 2: When Words Are Not Enough: Multimodal Idiom Disambiguation (https://arxiv.org/abs/2602.18652v1)
- [arxiv:ax-2026-02-20-4] DP-RFT: Learning to Generate Synthetic Text via Differentially Private Reinforcement Fine-Tuning (https://arxiv.org/abs/2602.18633v1)
- [arxiv:ax-2026-02-20-5] Narrating For You: Prompt-guided Audio-visual Narrating Face Generation Employing Multi-entangled Latent Space (https://arxiv.org/abs/2602.18618v1)
- [arxiv:ax-2026-02-20-6] Effect of Patch Size on Fine-Tuning Vision Transformers in Two-Dimensional and Three-Dimensional Medical Image Classification (https://arxiv.org/abs/2602.18614v1)
- [arxiv:ax-2026-02-20-7] Large Causal Models for Temporal Causal Discovery (https://arxiv.org/abs/2602.18662v1)
- [arxiv:ax-2026-02-20-8] Global Low-Rank, Local Full-Rank: The Holographic Encoding of Learned Algorithms (https://arxiv.org/abs/2602.18649v1)
- [arxiv:ax-2026-02-20-9] Information-Guided Noise Allocation for Efficient Diffusion Training (https://arxiv.org/abs/2602.18647v1)
- [arxiv:ax-2026-02-21-1] When Do LLM Preferences Predict Downstream Behavior? (https://arxiv.org/abs/2602.18971v1)
- [arxiv:ax-2026-02-21-10] YOLOv10-Based Multi-Task Framework for Hand Localization and Laterality Classification in Surgical Videos (https://arxiv.org/abs/2602.18959v1)
- [arxiv:ax-2026-02-21-11] Global Commander and Local Operative: A Dual-Agent Framework for Scene Navigation (https://arxiv.org/abs/2602.18941v1)
- [arxiv:ax-2026-02-21-12] Conditionally Site-Independent Neural Evolution of Antibody Sequences (https://arxiv.org/abs/2602.18982v1)
- [arxiv:ax-2026-02-21-13] Incremental Transformer Neural Processes (https://arxiv.org/abs/2602.18955v1)
- [arxiv:ax-2026-02-21-14] Toward Manifest Relationality in Transformers via Symmetry Reduction (https://arxiv.org/abs/2602.18948v1)
- [arxiv:ax-2026-02-21-15] Exponential Convergence of (Stochastic) Gradient Descent for Separable Logistic Regression (https://arxiv.org/abs/2602.18946v1)
- [arxiv:ax-2026-02-21-2] Robust and Efficient Tool Orchestration via Layered Execution Structures with Reflective Correction (https://arxiv.org/abs/2602.18968v1)
- [arxiv:ax-2026-02-21-3] Modularity is the Bedrock of Natural and Artificial Intelligence (https://arxiv.org/abs/2602.18960v1)
- [arxiv:ax-2026-02-21-4] INDUCTION: Finite-Structure Concept Synthesis in First-Order Logic (https://arxiv.org/abs/2602.18956v1)
- [arxiv:ax-2026-02-21-5] Whisper: Courtside Edition Enhancing ASR Performance Through LLM-Driven Context Generation (https://arxiv.org/abs/2602.18966v1)
- [arxiv:ax-2026-02-21-6] Yor-Sarc: A gold-standard dataset for sarcasm detection in a low-resource African language (https://arxiv.org/abs/2602.18964v1)
- [arxiv:ax-2026-02-21-7] Frame2Freq: Spectral Adapters for Fine-Grained Video Understanding (https://arxiv.org/abs/2602.18977v1)
- [arxiv:ax-2026-02-21-8] Face Presentation Attack Detection via Content-Adaptive Spatial Operators (https://arxiv.org/abs/2602.18965v1)
- [arxiv:ax-2026-02-21-9] Depth-Enhanced YOLO-SAM2 Detection for Reliable Ballast Insufficiency Identification (https://arxiv.org/abs/2602.18961v1)
- [arxiv:ax-2026-02-22-1] Time Series, Vision, and Language: Exploring the Limits of Alignment in Contrastive Representation Spaces (https://arxiv.org/abs/2602.19367v1)
- [arxiv:ax-2026-02-22-10] VCDF: A Validated Consensus-Driven Framework for Time Series Causal Discovery (https://arxiv.org/abs/2602.21381v1)
- [arxiv:ax-2026-02-22-11] Stable Deep Reinforcement Learning via Isotropic Gaussian Representations (https://arxiv.org/abs/2602.19373v1)
- [arxiv:ax-2026-02-22-12] Golden Layers and Where to Find Them: Improved Knowledge Editing for Large Language Models Via Layer Gradient Analysis (https://arxiv.org/abs/2602.20207v1)
- [arxiv:ax-2026-02-22-13] LLMs Can Learn to Reason Via Off-Policy RL (https://arxiv.org/abs/2602.19362v1)
- [arxiv:ax-2026-02-22-14] Active perception and disentangled representations allow continual, episodic zero and few-shot learning (https://arxiv.org/abs/2602.19355v1)
- [arxiv:ax-2026-02-22-15] Smooth Gate Functions for Soft Advantage Policy Optimization (https://arxiv.org/abs/2602.19345v1)
- [arxiv:ax-2026-02-22-2] PerSoMed: A Large-Scale Balanced Dataset for Persian Social Media Text Classification (https://arxiv.org/abs/2602.19333v1)
- [arxiv:ax-2026-02-22-3] Adaptive Data Augmentation with Multi-armed Bandit: Sample-Efficient Embedding Calibration for Implicit Pattern Recognition (https://arxiv.org/abs/2602.19385v1)
- [arxiv:ax-2026-02-22-4] Detector-in-the-Loop Tracking: Active Memory Rectification for Stable Glottic Opening Localization (https://arxiv.org/abs/2602.19380v1)
- [arxiv:ax-2026-02-22-5] Referring Layer Decomposition (https://arxiv.org/abs/2602.19358v1)
- [arxiv:ax-2026-02-22-6] MentalBlackboard: Evaluating Spatial Visualization via Mathematical Transformations (https://arxiv.org/abs/2602.19357v1)
- [arxiv:ax-2026-02-22-7] UP-Fuse: Uncertainty-guided LiDAR-Camera Fusion for 3D Panoptic Segmentation (https://arxiv.org/abs/2602.19349v1)
- [arxiv:ax-2026-02-22-8] MultiDiffSense: Diffusion-Based Multi-Modal Visuo-Tactile Image Generation Conditioned on Object Shape and Contact Pose (https://arxiv.org/abs/2602.19348v1)
- [arxiv:ax-2026-02-22-9] Spiking Graph Predictive Coding for Reliable OOD Generalization (https://arxiv.org/abs/2602.19392v1)
- [clawhub:ch-2026-02-16-1] Human Pages (https://clawhub.ai/human-pages-ai/humanpages)
- [clawhub:ch-2026-02-16-2] Audiomind (https://clawhub.ai/wells1137/audiomind)
- [clawhub:ch-2026-02-16-3] Paradiz (https://clawhub.ai/keeper1978/paradiz)
- [clawhub:ch-2026-02-16-4] 日本雅虎拍卖估价 (https://clawhub.ai/skills?q=yahoo-auction-estimator)
- [clawhub:ch-2026-02-16-5] ClawSea NFT Marketplace (https://clawhub.ai/fluxmira-moltbot/clawsea-market)
- [clawhub:ch-2026-02-16-6] Memoria Memory System (https://clawhub.ai/cuilinshen/memoria-system)
- [clawhub:ch-2026-02-17-1] Intelligence Ingestion (https://clawhub.ai/sarahmirrand001-oss/intelligence-ingestion)
- [clawhub:ch-2026-02-17-2] llm-eval-router (https://clawhub.ai/nissan/llm-eval-router)
- [clawhub:ch-2026-02-17-3] realtime-interact-overlay (https://clawhub.ai/LightCastlePro/realtime-interact-overlay)
- [clawhub:ch-2026-02-17-4] Creative Toolkit (https://clawhub.ai/jau123/creative-toolkit)
- [clawhub:ch-2026-02-18-1] Skill (https://clawhub.ai/efe-arv/sigil-security)
- [clawhub:ch-2026-02-18-2] Image Studio — AI Image Prompt System (https://clawhub.ai/danielblinker83-bot/image-studio)
- [clawhub:ch-2026-02-18-3] fastapi-studio-template (https://clawhub.ai/nissan/fastapi-studio-template)
- [clawhub:ch-2026-02-18-4] Baseline Kit (https://clawhub.ai/mike007jd/baseline-kit)
- [clawhub:ch-2026-02-18-5] Squarespace (https://clawhub.ai/byungkyu/squarespace)
- [clawhub:ch-2026-02-19-1] Post Job (https://clawhub.ai/zhangdong/post-job)
- [clawhub:ch-2026-02-19-2] Coding Agent Backup (https://clawhub.ai/nickchan0412/coding-agent-backup)
- [clawhub:ch-2026-02-19-3] Self Improving (https://clawhub.ai/ivangdavila/self-improving)
- [clawhub:ch-2026-02-19-4] Ghost Browser (https://clawhub.ai/neothelobster/neo-stealth-browser)
- [clawhub:ch-2026-02-19-5] Prayer Times Id (https://clawhub.ai/zckyachmd/prayer-times-id)
- [clawhub:ch-2026-02-19-6] virtual-remote-desktop (https://clawhub.ai/zhangxin15435/virtual-remote-desktop)
- [clawhub:ch-2026-02-19-7] Explorium AgentSource (https://clawhub.ai/yossigolan/explorium-agentsource)
- [clawhub:ch-2026-02-19-8] Ticket Monitor Ichinosuke (https://clawhub.ai/texka001/ticket-monitor-ichinosuke)
- [clawhub:ch-2026-02-20-1] AgentWeb.live — Global Business Directory (https://clawhub.ai/zerabic/agentweb)
- [clawhub:ch-2026-02-20-2] Agent Emacs (https://clawhub.ai/PiTZE/agent-emacs)
- [clawhub:ch-2026-02-20-3] Chainwatch (https://clawhub.ai/ppiankov/chainwatch)
- [clawhub:ch-2026-02-20-4] HeyLead (https://clawhub.ai/D4umak/heylead)
- [clawhub:ch-2026-02-20-5] Clack (https://clawhub.ai/fbn3799/clack)
- [clawhub:ch-2026-02-20-6] Host Hardening (https://clawhub.ai/ppiankov/server-host-hardening)
- [clawhub:ch-2026-02-21-1] Nova App Builder (https://clawhub.ai/zfdang/nova-app-builder)
- [clawhub:ch-2026-02-21-2] Mauritius Retail Prices (https://clawhub.ai/v7wm8gqgdr-design/mauritius-retail-prices)
- [clawhub:ch-2026-02-21-3] FairScale Solana (https://clawhub.ai/RisheeA/fairscale-solana)
- [clawhub:ch-2026-02-21-4] gog-test-demo (https://clawhub.ai/ph4ntonn/gog-test-demo)
- [clawhub:ch-2026-02-21-5] Recruiter Assistant (https://clawhub.ai/gakkiismywife/recruiter-assistant)
- [clawhub:ch-2026-02-21-6] OpenMM Portfolio (https://clawhub.ai/adacapo21/openmm-portfolio)
- [clawhub:ch-2026-02-21-7] EVC Team Relay (https://clawhub.ai/venturecrew/evc-team-relay)
- [clawhub:ch-2026-02-21-8] Temp Skill (https://clawhub.ai/wzratgit/temp-skill)
- [clawhub:ch-2026-02-22-1] Kekik Crawler (https://clawhub.ai/keyiflerolsun/kekik-crawler)
- [clawhub:ch-2026-02-22-2] Skill (https://clawhub.ai/askbeka/tentactl)
- [clawhub:ch-2026-02-22-3] Delx Ops Guardian (https://clawhub.ai/davidmosiah/delx-ops-guardian)
- [clawhub:ch-2026-02-22-4] TrustMyAgent (https://clawhub.ai/Anecdotes-Yair/trust-my-agent-ai)
- [clawhub:ch-2026-02-22-5] Neolata Memory Engine (https://clawhub.ai/Jeremiaheth/neolata-mem)
- [clawhub:ch-2026-02-22-6] Alicloud Ai Audio Tts (https://clawhub.ai/cinience/alicloud-ai-audio-tts)
- [clawhub:ch-2026-02-22-7] StandX CLI (https://clawhub.ai/wjllance/standx-cli)
- [clawhub:ch-2026-02-22-8] TuleBank (https://clawhub.ai/aromeoes/tulebank)
- [github:gh-2026-02-16-11] siteboon/claudecodeui (https://github.com/siteboon/claudecodeui)
- [github:gh-2026-02-17-1] liyupi/ai-guide (https://github.com/liyupi/ai-guide)
- [github:gh-2026-02-17-5] VectifyAI/PageIndex (https://github.com/VectifyAI/PageIndex)
- [github:gh-2026-02-17-7] katanemo/plano (https://github.com/katanemo/plano)
- [github:gh-2026-02-18-10] shareAI-lab/learn-claude-code (https://github.com/shareAI-lab/learn-claude-code)
- [github:gh-2026-02-18-2] huggingface/skills (https://github.com/huggingface/skills)
- [github:gh-2026-02-18-3] datawhalechina/hello-agents (https://github.com/datawhalechina/hello-agents)
- [github:gh-2026-02-18-5] NVIDIA/Megatron-LM (https://github.com/NVIDIA/Megatron-LM)
- [github:gh-2026-02-18-8] abhigyanpatwari/GitNexus (https://github.com/abhigyanpatwari/GitNexus)
- [github:gh-2026-02-20-1] moonshine-ai/moonshine (https://github.com/moonshine-ai/moonshine)
- [github:gh-2026-02-22-3] D4Vinci/Scrapling (https://github.com/D4Vinci/Scrapling)
- [github:gh-2026-02-22-4] obra/superpowers (https://github.com/obra/superpowers)
- [github:gh-2026-02-22-5] bytedance/deer-flow (https://github.com/bytedance/deer-flow)
- [github:gh-2026-02-22-6] ruvnet/claude-flow (https://github.com/ruvnet/claude-flow)
- [producthunt:ph-2026-02-16-1] Base44 Backend Platform (https://www.producthunt.com/products/base44?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-16-10] SearchSeal (https://www.producthunt.com/products/searchseal?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-16-11] MockAPI Dog (https://www.producthunt.com/products/mockapi-dog?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-16-12] HookWatch (https://www.producthunt.com/products/hookwatch?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-16-13] CoThou Autonomous Superagent (https://www.producthunt.com/products/seamlessity?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-16-14] Fixure | Security Decision Intelligence (https://www.producthunt.com/products/fixure?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-16-15] memories.sh (https://www.producthunt.com/products/memories-sh?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-16-16] Drop in (https://www.producthunt.com/products/drop-in-4?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-16-17] Jinee AI (https://www.producthunt.com/products/jinee-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-16-18] PromptScan (https://www.producthunt.com/products/promptscan?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-16-19] Promptly (https://www.producthunt.com/products/promptly-19?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-16-2] Toolspend (https://www.producthunt.com/products/toolspend?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-16-20] PokePerps (https://www.producthunt.com/products/pokeperps?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-16-21] Queryline (https://www.producthunt.com/products/queryline?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-16-22] Kagura AI (https://www.producthunt.com/products/kagura-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-16-23] CabbageSEO (https://www.producthunt.com/products/cabbageseo?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-16-24] Redirections (https://www.producthunt.com/products/redirections?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-16-25] Juno - AI Creative Coding (https://www.producthunt.com/products/juno-ai-creative-coding?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-16-3] NVIDIA PersonaPlex (https://www.producthunt.com/products/nvidia?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-16-4] JDoodle.ai MCP (https://www.producthunt.com/products/jdoodle-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-16-5] PenguinBot AI (https://www.producthunt.com/products/penguinbot-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-16-6] Agent Bar (https://www.producthunt.com/products/agent-bar?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-16-7] Marketing Agents Squad (https://www.producthunt.com/products/marketing-agents-squad?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-16-8] chowder.dev (https://www.producthunt.com/products/chowder-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-16-9] Enough Cream (https://www.producthunt.com/products/enough-cream?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-17-1] Figr AI (https://www.producthunt.com/products/figr-design-research-simplified?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-17-10] JustScribe (https://www.producthunt.com/products/justscribe?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-17-11] HostedClaws (https://www.producthunt.com/products/hostedclaws?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-17-12] VidClaw (https://www.producthunt.com/products/vidclaw?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-17-13] Drivebase (https://www.producthunt.com/products/drivebase?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-17-14] TransLite (https://www.producthunt.com/products/translite-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-17-15] MetMe (https://www.producthunt.com/products/metme?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-17-16] Synra (https://www.producthunt.com/products/synra-managed-mcp-server?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-17-17] AI Tech Packs (https://www.producthunt.com/products/ai-tech-packs?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-17-18] AI Hotkeys (https://www.producthunt.com/products/ai-hotkeys?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-17-19] Auden (https://www.producthunt.com/products/auden?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-17-2] Boost.space v5 (https://www.producthunt.com/products/boost-space?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-17-20] Subterranean (https://www.producthunt.com/products/subterranean-3?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-17-21] doXmind (https://www.producthunt.com/products/doxmind?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-17-22] Scoutflo (https://www.producthunt.com/products/scoutflo?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-17-23] OrcaSheets (https://www.producthunt.com/products/orcasheets?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-17-24] Synergy - Web to Figma (https://www.producthunt.com/products/synergy-web-to-figma?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-17-25] Lightning Rod: Training Data From News (https://www.producthunt.com/products/training-data-generator?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-17-26] OpenClaw Map – Discover OpenClaw Tools (https://www.producthunt.com/products/openclaw-map-discover-openclaw-tools?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-17-3] Qwen3.5 (https://www.producthunt.com/products/qwen3?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-17-4] Layers (https://www.producthunt.com/products/layers-6?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-17-5] MiniMax-M2.5 (https://www.producthunt.com/products/minimax-m2-5?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-17-6] claude-devtools (https://www.producthunt.com/products/claude-devtools?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-17-7] Vela (https://www.producthunt.com/products/vela-4?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-17-8] Brainstream (https://www.producthunt.com/products/brainstream?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-17-9] Agent Monitor (https://www.producthunt.com/products/agent-monitor-track-ai-traffic?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-18-1] Sonnet 4.6 (https://www.producthunt.com/products/claude?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-18-2] Moda (https://www.producthunt.com/products/moda-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-18-3] Omnia (https://www.producthunt.com/products/omnia-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-18-4] Flixier Generate AI Video in Timeline (https://www.producthunt.com/products/flixier?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-18-5] ClawMetry for OpenClaw (https://www.producthunt.com/products/clawmetry?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-18-6] Design Rails (https://www.producthunt.com/products/design-rails-ai-native-brand-in-mins?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-19-1] Clawi.ai (https://www.producthunt.com/products/clawi-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-19-10] isFake.ai (https://www.producthunt.com/products/isfake-ai-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-19-11] Ningenie (https://www.producthunt.com/products/ningenie?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-19-12] Yandex AI Türkiye (https://www.producthunt.com/products/yandex-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-19-13] Facts Hero (https://www.producthunt.com/products/facts-hero?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-19-14] Advertise at the speed of thought (https://www.producthunt.com/products/ad-vertly?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-19-15] AiArtist (https://www.producthunt.com/products/aiartist?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-19-16] QuantumComp Webflow Website Template (https://www.producthunt.com/products/quantumcomp-webflow-website-template?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-19-17] Turbotic Automation AI OPEN SOURCE (https://www.producthunt.com/products/turbotic-automation-ai-open-source?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-19-2] Reloop (https://www.producthunt.com/products/reloop?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-19-3] Monologue for iOS (https://www.producthunt.com/products/monologue-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-19-4] FF Designer (https://www.producthunt.com/products/flutterflow?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-19-5] Kollect Voice Agent (https://www.producthunt.com/products/kollect-voice-agent?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-19-6] Decks For Good (https://www.producthunt.com/products/decks-for-good?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-19-7] AgentReady (https://www.producthunt.com/products/agentready-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-19-8] Mengram (https://www.producthunt.com/products/mengram?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-19-9] Feedix (https://www.producthunt.com/products/feedix?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-20-1] Architect by Lyzr (https://www.producthunt.com/products/architect?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-20-10] Coasty (https://www.producthunt.com/products/coasty?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-20-11] Anythink (https://www.producthunt.com/products/anythink?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-20-12] IPAware (https://www.producthunt.com/products/ipaware?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-20-13] Sprout Budget (https://www.producthunt.com/products/sprout-budget?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-20-14] fasrad (https://www.producthunt.com/products/fasrad-hosted-agents?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-20-15] WP Multitool (https://www.producthunt.com/products/wp-multitool?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-20-2] Claudebin (https://www.producthunt.com/products/claudebin?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-20-3] keychains.dev (https://www.producthunt.com/products/keychain-dev?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-20-4] Guideless (https://www.producthunt.com/products/guideless?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-20-5] NotchPrompt (https://www.producthunt.com/products/notchprompt?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-20-6] Repaint (https://www.producthunt.com/products/repaint-ai-website-builder?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-20-7] UI Inspector (https://www.producthunt.com/products/ui-inspector?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-20-8] moCODE (https://www.producthunt.com/products/mocode?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-20-9] trnscrb (https://www.producthunt.com/products/trnscrb?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-21-1] Rork Max (https://www.producthunt.com/products/rork-app-for-ios?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-21-10] Awshar AI (https://www.producthunt.com/products/awshar-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-21-11] Claude Code Security (https://www.producthunt.com/products/claude-code?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-21-12] MeetClaw AI (https://www.producthunt.com/products/meetclaw-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-21-13] WayOut - Walk to Earn Screen Time (https://www.producthunt.com/products/wayout-walk-to-earn-screen-time?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-21-14] Pika AI Selves (https://www.producthunt.com/products/pika-ai-selves?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-21-15] PickedVids.com (https://www.producthunt.com/products/pickedvids-com?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-21-2] Lyria 3 by Google Deepmind (https://www.producthunt.com/products/lyria-3-by-google-deepmind?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-21-3] git-lrc (https://www.producthunt.com/products/git-lrc?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-21-4] Prism Videos (https://www.producthunt.com/products/prism-videos?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-21-5] Woise (https://www.producthunt.com/products/woise-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-21-6] KraftCV (https://www.producthunt.com/products/kraftcv?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-21-7] Postly-ai (https://www.producthunt.com/products/postly-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-21-8] ads Campaign Ops with AI at every step. (https://www.producthunt.com/products/stish-from-start-to-finish?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-21-9] Huefold Game (https://www.producthunt.com/products/huefold-game?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-22-10] DryCast (https://www.producthunt.com/products/drycast?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-22-11] TIMPs (https://www.producthunt.com/products/timps?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-22-12] OpenCharts (https://www.producthunt.com/products/opencharts?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-22-13] ClawCloud (https://www.producthunt.com/products/clawcloud?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-22-14] zymplio: Master your WordPress Stack (https://www.producthunt.com/products/zymplio-master-your-wordpress-stack?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-22-15] CatsMe 2.0 – AI Cat Health from a Photo (https://www.producthunt.com/products/catsme?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-22-16] Okiela (https://www.producthunt.com/products/okiela?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-22-2] Straion (https://www.producthunt.com/products/straion?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-22-3] Tidy (https://www.producthunt.com/products/tidy-3?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-22-4] Ashera AI (https://www.producthunt.com/products/index-of-ashera?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-22-5] Verly (https://www.producthunt.com/products/verly-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-22-6] Remalt (https://www.producthunt.com/products/remalt?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-22-7] Delta IQ (https://www.producthunt.com/products/delta-iq?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-22-8] Voice Notes to Text - SotiTalk (https://www.producthunt.com/products/voice-notes-to-text-sotitalk?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-02-22-9] Vocal Division (https://www.producthunt.com/products/vocal-division?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
