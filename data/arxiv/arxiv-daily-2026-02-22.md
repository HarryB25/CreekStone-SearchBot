# arXiv AI 论文日报 | 2026-02-22

> 共 15 篇论文，由AI自动总结

## 📑 目录

- [cs.LG](#csLG) (7 篇)
- [cs.CV](#csCV) (6 篇)
- [cs.AI](#csAI) (1 篇)
- [cs.CL](#csCL) (1 篇)

---

## cs.AI

## [1. Time Series, Vision, and Language: Exploring the Limits of Alignment in Contrastive Representation Spaces](https://arxiv.org/abs/2602.19367v1)

**作者**：Pratham Yashwante, Rose Yu  
**分类**：cs.AI, cs.CV  
**发布时间**：2026-02-22

### 📄 论文摘要

The Platonic Representation Hypothesis posits that learned representations from models trained on different modalities converge to a shared latent structure of the world. However, this hypothesis has largely been examined in vision and language, and it remains unclear whether time series participate in such convergence. We first examine this in a trimodal setting and find that independently pretrained time series, vision, and language encoders exhibit near-orthogonal geometry in the absence of explicit coupling. We then apply post-hoc alignment by training projection heads over frozen encoders using contrastive learning, and analyze the resulting representations with respect to geometry, scaling behavior, and dependence on information density and input modality characteristics. Our investigation reveals that overall alignment in contrastive representation spaces improves with model size, but this alignment is asymmetric: time series align more strongly with visual representations than with text, and images can act as effective intermediaries between time series and language. We further see that richer textual descriptions improve alignment only up to a threshold; training on denser captions does not lead to further improvement. Analogous effects are observed for visual representations. Our findings shed light on considerations for building multimodal systems involving non-conventional data modalities beyond vision and language.

### 🤖 AI 总结

**一句话总结**：论文发现时间序列、视觉与语言的预训练表征在未显式耦合时几乎正交，但可通过冻结编码器+对比学习投影头实现后验对齐，且对齐呈现规模提升与模态非对称性。

**研究动机**：“表征趋同/柏拉图表征假说”多在视觉-语言上验证，尚不清楚时间序列是否也会与其他模态共享潜在结构。作者希望系统刻画三模态在对比表征空间中的可对齐性边界及其影响因素。

**核心方法**：先在三模态（时间序列/图像/文本）上分析各自独立预训练编码器的几何关系，观察是否天然对齐；再冻结编码器，仅训练投影头进行对比学习式的后验对齐，并从几何、规模律、信息密度（更丰富描述/更密集caption等）与模态特性角度评估对齐效果。

**主要结论**：对比空间整体对齐度随模型规模增大而提升，但存在显著非对称：时间序列更容易对齐到视觉而非文本，且图像可作为时间序列与语言之间的有效“中介”。更丰富的文本/视觉描述对对齐有帮助但存在阈值，超过一定信息密度后继续加密caption收益不再增长。

**关键词**：多模态表示对齐, 时间序列编码器, 视觉-语言对齐, 三模态学习, 后验对齐, 投影头, 冻结编码器, 表示几何, 缩放规律, 信息密度

**评分**：21

**论文链接**：[查看原文](https://arxiv.org/abs/2602.19367v1) | [下载PDF](https://arxiv.org/pdf/2602.19367v1.pdf)

---

## cs.CL

## [2. PerSoMed: A Large-Scale Balanced Dataset for Persian Social Media Text Classification](https://arxiv.org/abs/2602.19333v1)

**作者**：Isun Chehreh, Ebrahim Ansari  
**分类**：cs.CL, cs.IR, cs.SI  
**发布时间**：2026-02-22

### 📄 论文摘要

This research introduces the first large-scale, well-balanced Persian social media text classification dataset, specifically designed to address the lack of comprehensive resources in this domain. The dataset comprises 36,000 posts across nine categories (Economic, Artistic, Sports, Political, Social, Health, Psychological, Historical, and Science & Technology), each containing 4,000 samples to ensure balanced class distribution. Data collection involved 60,000 raw posts from various Persian social media platforms, followed by rigorous preprocessing and hybrid annotation combining ChatGPT-based few-shot prompting with human verification. To mitigate class imbalance, we employed undersampling with semantic redundancy removal and advanced data augmentation strategies integrating lexical replacement and generative prompting. We benchmarked several models, including BiLSTM, XLM-RoBERTa (with LoRA and AdaLoRA adaptations), FaBERT, SBERT-based architectures, and the Persian-specific TookaBERT (Base and Large). Experimental results show that transformer-based models consistently outperform traditional neural networks, with TookaBERT-Large achieving the best performance (Precision: 0.9622, Recall: 0.9621, F1- score: 0.9621). Class-wise evaluation further confirms robust performance across all categories, though social and political texts exhibited slightly lower scores due to inherent ambiguity. This research presents a new high-quality dataset and provides comprehensive evaluations of cutting-edge models, establishing a solid foundation for further developments in Persian NLP, including trend analysis, social behavior modeling, and user classification. The dataset is publicly available to support future research endeavors.

### 🤖 AI 总结

**一句话总结**：提出并公开了一个首个大规模、类别均衡的波斯语社交媒体文本分类数据集PerSoMed（36K/9类），并系统评测多种模型，TookaBERT-Large取得最佳效果。

**研究动机**：波斯语社交媒体文本分类缺乏规模足够且类别均衡的高质量公开数据，限制了相关NLP研究与应用发展。

**核心方法**：从多平台采集6万原始帖子，经严格预处理后用“ChatGPT少样本标注+人工复核”的混合标注生成9类各4000条；通过语义冗余去除的欠采样与结合词汇替换/生成式提示的数据增强缓解不均衡，并基准测试BiLSTM、XLM-R(LoRA/AdaLoRA)、FaBERT、SBERT与TookaBERT等模型。

**主要结论**：Transformer类模型整体显著优于传统神经网络，其中TookaBERT-Large达到最高F1=0.9621；按类评估显示总体稳健，但社交与政治类因语义歧义略低，数据集为后续波斯语社媒分析与用户建模等研究提供基础。

**关键词**：社交媒体文本分类, 数据集构建, 类别均衡, 混合标注, 少样本提示, 数据增强, 欠采样, 语义冗余去除, 参数高效微调（LoRA）

**评分**：21

**论文链接**：[查看原文](https://arxiv.org/abs/2602.19333v1) | [下载PDF](https://arxiv.org/pdf/2602.19333v1.pdf)

---

## cs.CV

## [3. Adaptive Data Augmentation with Multi-armed Bandit: Sample-Efficient Embedding Calibration for Implicit Pattern Recognition](https://arxiv.org/abs/2602.19385v1)

**作者**：Minxue Tang, Yangyang Yu, Aolin Ding 等 5 位作者  
**分类**：cs.CV, cs.CL, cs.LG  
**发布时间**：2026-02-22

### 📄 论文摘要

Recognizing implicit visual and textual patterns is essential in many real-world applications of modern AI. However, tackling long-tail pattern recognition tasks remains challenging for current pre-trained foundation models such as LLMs and VLMs. While finetuning pre-trained models can improve accuracy in recognizing implicit patterns, it is usually infeasible due to a lack of training data and high computational overhead. In this paper, we propose ADAMAB, an efficient embedding calibration framework for few-shot pattern recognition. To maximally reduce the computational costs, ADAMAB trains embedder-agnostic light-weight calibrators on top of fixed embedding models without accessing their parameters. To mitigate the need for large-scale training data, we introduce an adaptive data augmentation strategy based on the Multi-Armed Bandit (MAB) mechanism. With a modified upper confidence bound algorithm, ADAMAB diminishes the gradient shifting and offers theoretically guaranteed convergence in few-shot training. Our multi-modal experiments justify the superior performance of ADAMAB, with up to 40% accuracy improvement when training with less than 5 initial data samples of each class.

### 🤖 AI 总结

**一句话总结**：ADAMAB通过在冻结的嵌入模型上训练轻量校准器，并用基于多臂老虎机的自适应数据增强，在极少样本下显著提升隐式模式识别准确率。

**研究动机**：长尾的隐式视觉/文本模式识别对现有预训练基础模型仍具挑战，而直接微调往往受限于数据稀缺与算力成本过高。

**核心方法**：提出嵌入器无关的轻量校准器（不访问/更新底座模型参数）以低成本进行embedding校准；同时用改进的UCB多臂老虎机策略自适应选择数据增强方式，减少few-shot训练中的梯度漂移并给出收敛保证。

**主要结论**：多模态实验表明ADAMAB在每类少于5个初始样本时仍能稳定收敛并取得显著收益，最高可带来约40%的准确率提升。

**关键词**：隐式模式识别, 长尾识别, 小样本学习, 嵌入校准, 参数高效微调, 自适应数据增强, 多臂老虎机（MAB）, 冻结嵌入模型, 轻量校准器, 多模态学习, 基础模型（LLM/VLM）

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2602.19385v1) | [下载PDF](https://arxiv.org/pdf/2602.19385v1.pdf)

---

## [4. Detector-in-the-Loop Tracking: Active Memory Rectification for Stable Glottic Opening Localization](https://arxiv.org/abs/2602.19380v1)

**作者**：Huayu Wang, Bahaa Alattar, Cheng-Yen Yang 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-22

### 📄 论文摘要

Temporal stability in glottic opening localization remains challenging due to the complementary weaknesses of single-frame detectors and foundation-model trackers: the former lacks temporal context, while the latter suffers from memory drift. Specifically, in video laryngoscopy, rapid tissue deformation, occlusions, and visual ambiguities in emergency settings require a robust, temporally aware solution that can prevent progressive tracking errors. We propose Closed-Loop Memory Correction (CL-MC), a detector-in-the-loop framework that supervises Segment Anything Model 2(SAM2) through confidence-aligned state decisions and active memory rectification. High-confidence detections trigger semantic resets that overwrite corrupted tracker memory, effectively mitigating drift accumulation with a training-free foundation tracker in complex endoscopic scenes. On emergency intubation videos, CL-MC achieves state-of-the-art performance, significantly reducing drift and missing rate compared with the SAM2 variants and open loop based methods. Our results establish memory correction as a crucial component for reliable clinical video tracking. Our code will be available in https://github.com/huayuww/CL-MR.

### 🤖 AI 总结

**一句话总结**：提出Detector-in-the-Loop的闭环记忆校正（CL-MC），用高置信检测对SAM2跟踪器进行语义重置与记忆纠偏，从而稳定定位声门开口并显著减少漂移与漏检。

**研究动机**：单帧检测器缺乏时序上下文，而基础模型跟踪器易发生记忆漂移；在急诊喉镜视频中存在快速形变、遮挡与模糊，导致跟踪误差会随时间累积。

**核心方法**：构建CL-MC闭环框架：将检测器输出的置信度与状态决策对齐，在检测高置信时触发“语义重置”，用检测结果覆盖/纠正SAM2的内部记忆以主动消除漂移；整体为training-free地监督基础跟踪器。

**主要结论**：在急诊插管喉镜视频上达到SOTA，相比SAM2变体与开环方法显著降低漂移与缺失率；结果表明“记忆校正”是临床视频可靠跟踪的关键组件。

**关键词**：闭环记忆校正, 视频喉镜, 跟踪稳定性, 语义重置, 内循环检测器, 内存漂移, 紧急插管, 复杂内窥镜场景

**评分**：35

**论文链接**：[查看原文](https://arxiv.org/abs/2602.19380v1) | [下载PDF](https://arxiv.org/pdf/2602.19380v1.pdf)

---

## [5. Referring Layer Decomposition](https://arxiv.org/abs/2602.19358v1)

**作者**：Fangyi Chen, Yaojie Shen, Lu Xu 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-22

### 📄 论文摘要

Precise, object-aware control over visual content is essential for advanced image editing and compositional generation. Yet, most existing approaches operate on entire images holistically, limiting the ability to isolate and manipulate individual scene elements. In contrast, layered representations, where scenes are explicitly separated into objects, environmental context, and visual effects, provide a more intuitive and structured framework for interpreting and editing visual content. To bridge this gap and enable both compositional understanding and controllable editing, we introduce the Referring Layer Decomposition (RLD) task, which predicts complete RGBA layers from a single RGB image, conditioned on flexible user prompts, such as spatial inputs (e.g., points, boxes, masks), natural language descriptions, or combinations thereof. At the core is the RefLade, a large-scale dataset comprising 1.11M image-layer-prompt triplets produced by our scalable data engine, along with 100K manually curated, high-fidelity layers. Coupled with a perceptually grounded, human-preference-aligned automatic evaluation protocol, RefLade establishes RLD as a well-defined and benchmarkable research task. Building on this foundation, we present RefLayer, a simple baseline designed for prompt-conditioned layer decomposition, achieving high visual fidelity and semantic alignment. Extensive experiments show our approach enables effective training, reliable evaluation, and high-quality image decomposition, while exhibiting strong zero-shot generalization capabilities.

### 🤖 AI 总结

**一句话总结**：提出“指代式图层分解”(RLD)任务：在用户提示（语言/点框mask等）条件下，从单张RGB图像预测可编辑的完整RGBA分层表示，并给出数据集与基线模型推动可评测研究。

**研究动机**：现有图像编辑/生成多以整图为单位，难以精确隔离与操控单个对象、环境与效果；而显式分层更符合人类编辑流程但缺少统一任务定义与大规模基准。

**核心方法**：定义RLD任务并构建RefLade数据集（约111万图像-图层-提示三元组+10万高保真人工层），配套“感知+人类偏好对齐”的自动评测协议；在此基础上提出RefLayer作为提示条件的分层分解基线模型，实现从RGB到多RGBA层的预测。

**主要结论**：实验表明该数据与评测使RLD成为可训练、可可靠评测的基准任务，RefLayer能产生高保真且语义对齐的分层结果，并展现较强零样本泛化与可控编辑潜力。

**关键词**：指代式图层分解, 提示条件分解, 分层场景表示, 组合式图像生成, 空间提示（点/框/掩膜）, 自然语言提示, 大规模图像-图层-提示数据集, 人类偏好对齐评测, 零样本泛化

**评分**：36

**论文链接**：[查看原文](https://arxiv.org/abs/2602.19358v1) | [下载PDF](https://arxiv.org/pdf/2602.19358v1.pdf)

---

## [6. MentalBlackboard: Evaluating Spatial Visualization via Mathematical Transformations](https://arxiv.org/abs/2602.19357v1)

**作者**：Nilay Yilmaz, Maitreya Patel, Naga Sai Abhiram Kusumba 等 5 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-02-22

### 📄 论文摘要

Spatial visualization is the mental ability to imagine, transform, and manipulate the spatial characteristics of objects and actions. This intelligence is a part of human cognition where actions and perception are connected on a mental level. To explore whether state-of-the-art Vision-Language Models (VLMs) exhibit this ability, we develop MentalBlackboard, an open-ended spatial visualization benchmark for Paper Folding and Hole Punching tests within two core tasks: prediction and planning. Our prediction experiments reveal that models struggle with applying symmetrical transformations, even when they predict the sequence of unfolding steps correctly. Also, rotations introduce a significant challenge to the physical situational awareness for models. The planning task reveals limitations of models in analyzing symmetrical relationships and in implementing the multi-stage symmetry process, with Claude Opus 4.1 achieving the highest planning score at an accuracy of 10\%. The top-performing model, o3, attains a peak performance of 71.6\% on the generalization task, which does not require spatial visualization but transfers spatial data; however, it achieves only 25\% accuracy on text-based prediction tasks.

### 🤖 AI 总结

**一句话总结**：MentalBlackboard 基准用于评估VLM在纸折叠/打孔等空间可视化任务中的“预测+规划”能力，结果显示主流模型在对称变换与旋转推理上显著薄弱。

**研究动机**：空间可视化是人类认知中将动作与感知联结的关键能力，但现有VLM是否具备对物体进行心智变换（对称、旋转、展开）的能力仍缺少系统评测。

**核心方法**：提出开放式基准 MentalBlackboard，覆盖纸折叠与打孔两类题型，并设置预测任务（给定折叠/展开过程推断最终结果）与规划任务（反推或设计多阶段对称过程）以测试模型的空间变换推理。

**主要结论**：实验表明模型常在对称变换应用上失败，即使能正确预测展开步骤；旋转显著削弱其物理情境理解。规划任务整体准确率很低（如 Claude Opus 4.1 约10%），而 o3 在不要求空间可视化、仅迁移空间数据的泛化任务上可达71.6%，但在纯文本预测上仅约25%。

**关键词**：空间可视化, 空间推理, 视觉语言模型评测, 空间推理基准, 旋转变换, 规划任务, 预测任务, 泛化评测

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2602.19357v1) | [下载PDF](https://arxiv.org/pdf/2602.19357v1.pdf)

---

## [7. UP-Fuse: Uncertainty-guided LiDAR-Camera Fusion for 3D Panoptic Segmentation](https://arxiv.org/abs/2602.19349v1)

**作者**：Rohit Mohan, Florian Drews, Yakov Miron 等 5 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-02-22

### 📄 论文摘要

LiDAR-camera fusion enhances 3D panoptic segmentation by leveraging camera images to complement sparse LiDAR scans, but it also introduces a critical failure mode. Under adverse conditions, degradation or failure of the camera sensor can significantly compromise the reliability of the perception system. To address this problem, we introduce UP-Fuse, a novel uncertainty-aware fusion framework in the 2D range-view that remains robust under camera sensor degradation, calibration drift, and sensor failure. Raw LiDAR data is first projected into the range-view and encoded by a LiDAR encoder, while camera features are simultaneously extracted and projected into the same shared space. At its core, UP-Fuse employs an uncertainty-guided fusion module that dynamically modulates cross-modal interaction using predicted uncertainty maps. These maps are learned by quantifying representational divergence under diverse visual degradations, ensuring that only reliable visual cues influence the fused representation. The fused range-view features are decoded by a novel hybrid 2D-3D transformer that mitigates spatial ambiguities inherent to the 2D projection and directly predicts 3D panoptic segmentation masks. Extensive experiments on Panoptic nuScenes, SemanticKITTI, and our introduced Panoptic Waymo benchmark demonstrate the efficacy and robustness of UP-Fuse, which maintains strong performance even under severe visual corruption or misalignment, making it well suited for robotic perception in safety-critical settings.

### 🤖 AI 总结

**一句话总结**：UP-Fuse 提出一种不确定性引导的 LiDAR-相机融合框架，在相机退化、标定漂移或失效时仍能稳健进行 3D 全景分割。

**研究动机**：传统 LiDAR-相机融合虽能提升精度，但在雨雾、遮挡、曝光异常或标定偏移等情况下会引入错误视觉信息，导致感知系统可靠性显著下降。

**核心方法**：将 LiDAR 投影到 2D range-view 并编码，同时提取并投影相机特征到同一空间；通过学习的不确定性图衡量视觉退化下的表征分歧，动态抑制不可靠的跨模态交互；再用混合 2D-3D Transformer 解码以缓解 2D 投影带来的空间歧义并直接预测 3D panoptic 掩码。

**主要结论**：在 Panoptic nuScenes、SemanticKITTI 和新增的 Panoptic Waymo 上，UP-Fuse 在正常条件下保持强性能，并在严重视觉腐蚀、错位或相机故障时显著优于常规融合方法，体现出更高的安全关键场景鲁棒性。

**关键词**：激光雷达-相机融合, 三维全景分割, 不确定性引导融合, 跨模态交互调制, 不确定性图, 二维距离视图, 传感器退化鲁棒性, 标定漂移鲁棒性, 视觉腐蚀鲁棒性, 表征差异度量, 机器人安全关键感知

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2602.19349v1) | [下载PDF](https://arxiv.org/pdf/2602.19349v1.pdf)

---

## [8. MultiDiffSense: Diffusion-Based Multi-Modal Visuo-Tactile Image Generation Conditioned on Object Shape and Contact Pose](https://arxiv.org/abs/2602.19348v1)

**作者**：Sirine Bhouri, Lan Wei, Jian-Qing Zheng 等 4 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-02-22

### 📄 论文摘要

Acquiring aligned visuo-tactile datasets is slow and costly, requiring specialised hardware and large-scale data collection. Synthetic generation is promising, but prior methods are typically single-modality, limiting cross-modal learning. We present MultiDiffSense, a unified diffusion model that synthesises images for multiple vision-based tactile sensors (ViTac, TacTip, ViTacTip) within a single architecture. Our approach uses dual conditioning on CAD-derived, pose-aligned depth maps and structured prompts that encode sensor type and 4-DoF contact pose, enabling controllable, physically consistent multi-modal synthesis. Evaluating on 8 objects (5 seen, 3 novel) and unseen poses, MultiDiffSense outperforms a Pix2Pix cGAN baseline in SSIM by +36.3% (ViTac), +134.6% (ViTacTip), and +64.7% (TacTip). For downstream 3-DoF pose estimation, mixing 50% synthetic with 50% real halves the required real data while maintaining competitive performance. MultiDiffSense alleviates the data-collection bottleneck in tactile sensing and enables scalable, controllable multi-modal dataset generation for robotic applications.

### 🤖 AI 总结

**一句话总结**：MultiDiffSense 用一个统一的扩散模型，在 CAD 深度与接触位姿条件下可控生成多种视觉触觉传感器的合成图像，并显著提升生成质量与下游位姿学习的数据效率。

**研究动机**：对齐的视觉-触觉数据采集昂贵且耗时，限制触觉学习规模化；现有合成方法多为单模态，难以支持跨传感器/跨模态学习与可控生成。

**核心方法**：提出统一扩散生成框架，同时生成 ViTac、TacTip、ViTacTip 等多传感器图像；采用“双条件”输入：由 CAD 推得并与姿态对齐的深度图作为形状/几何约束，以及包含传感器类型与4-DoF接触位姿的结构化提示以实现可控、物理一致的合成。

**主要结论**：在已见/新物体与未见位姿上，较 Pix2Pix cGAN 在 SSIM 上大幅提升（不同传感器提升 36.3%~134.6%）；在 3-DoF 位姿估计任务中，50%合成+50%真实数据可在保持性能的同时将真实数据需求减半，缓解触觉数据采集瓶颈。

**关键词**：Diffusion, 多模态生成, 视觉-触觉, 触觉图像合成, 条件生成, 深度图条件, CAD形状先验, 接触位姿条件, 跨模态学习, 合成数据增强, 机器人触觉感知, 位姿估计

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2602.19348v1) | [下载PDF](https://arxiv.org/pdf/2602.19348v1.pdf)

---

## cs.LG

## [9. Spiking Graph Predictive Coding for Reliable OOD Generalization](https://arxiv.org/abs/2602.19392v1)

**作者**：Jing Ren, Jiapeng Du, Bowen Li 等 9 位作者  
**分类**：cs.LG, cs.SI  
**发布时间**：2026-02-22

### 📄 论文摘要

Graphs provide a powerful basis for modeling Web-based relational data, with expressive GNNs to support the effective learning in dynamic web environments. However, real-world deployment is hindered by pervasive out-of-distribution (OOD) shifts, where evolving user activity and changing content semantics alter feature distributions and labeling criteria. These shifts often lead to unstable or overconfident predictions, undermining the trustworthiness required for Web4Good applications. Achieving reliable OOD generalization demands principled and interpretable uncertainty estimation; however, existing methods are largely post-hoc, insensitive to distribution shifts, and unable to explain where uncertainty arises especially in high-stakes settings. To address these limitations, we introduce SpIking GrapH predicTive coding (SIGHT), an uncertainty-aware plug-in graph learning module for reliable OOD Generalization. SIGHT performs iterative, error-driven correction over spiking graph states, enabling models to expose internal mismatch signals that reveal where predictions become unreliable. Across multiple graph benchmarks and diverse OOD scenarios, SIGHT consistently enhances predictive accuracy, uncertainty estimation, and interpretability when integrated with GNNs.

### 🤖 AI 总结

**一句话总结**：SIGHT 通过脉冲式图预测编码的迭代误差校正机制，让GNN在分布外（OOD）场景下同时提升准确性、可靠不确定性估计与可解释性。

**研究动机**：真实图数据（如Web环境）存在频繁的OOD分布漂移，会导致GNN预测不稳定且过度自信，影响高风险应用的可信部署。现有不确定性方法多为事后校准、对分布变化不敏感，且难以解释不确定性来源。

**核心方法**：提出可插拔模块SIGHT，在图的“脉冲/尖峰”状态上进行迭代、误差驱动的预测编码更新，通过内部“失配/残差信号”对表示进行纠错并显式暴露不确定性来源。将其集成到各类GNN中，以迭代推理过程产生更稳健的预测与可解释的置信度。

**主要结论**：在多个图基准与多种OOD设置下，SIGHT集成后可稳定提升预测精度、不确定性估计质量和解释性，表明误差驱动的内部校正对可靠OOD泛化有效。

**关键词**：图神经网络, 图表示学习, 分布外泛化, 分布漂移鲁棒性, 不确定性估计, 不确定性校准, 可解释性, 预测编码, 脉冲神经网络, 迭代误差校正, 动态图学习

**评分**：24

**论文链接**：[查看原文](https://arxiv.org/abs/2602.19392v1) | [下载PDF](https://arxiv.org/pdf/2602.19392v1.pdf)

---

## [10. VCDF: A Validated Consensus-Driven Framework for Time Series Causal Discovery](https://arxiv.org/abs/2602.21381v1)

**作者**：Gene Yu, Ce Guo, Wayne Luk  
**分类**：cs.LG, cs.AI, cs.CE  
**发布时间**：2026-02-22

### 📄 论文摘要

Time series causal discovery is essential for understanding dynamic systems, yet many existing methods remain sensitive to noise, non-stationarity, and sampling variability. We propose the Validated Consensus-Driven Framework (VCDF), a simple and method-agnostic layer that improves robustness by evaluating the stability of causal relations across blocked temporal subsets. VCDF requires no modification to base algorithms and can be applied to methods such as VAR-LiNGAM and PCMCI. Experiments on synthetic datasets show that VCDF improves VAR-LiNGAM by approximately 0.08-0.12 in both window and summary F1 scores across diverse data characteristics, with gains most pronounced for moderate-to-long sequences. The framework also benefits from longer sequences, yielding up to 0.18 absolute improvement on time series of length 1000 and above. Evaluations on simulated fMRI data and IT-monitoring scenarios further demonstrate enhanced stability and structural accuracy under realistic noise conditions. VCDF provides an effective reliability layer for time series causal discovery without altering underlying modeling assumptions.

### 🤖 AI 总结

**一句话总结**：VCDF通过在时间分块子序列上做稳定性验证与共识聚合，为现有时间序列因果发现算法提供一层不改模型的鲁棒性增强。

**研究动机**：现有时间序列因果发现方法容易受噪声、非平稳性和采样波动影响，导致因果边不稳定、结果可重复性差。需要一种与具体算法无关、能提升因果关系可靠性的通用框架。

**核心方法**：VCDF将时间序列划分为多个被阻断（blocked）的时间子集，在各子集上重复运行任意基础因果发现算法（如VAR-LiNGAM、PCMCI），再依据因果关系在不同子集中的一致性进行验证与共识筛选。该框架作为“外层可靠性层”工作，不要求修改底层算法假设或训练流程。

**主要结论**：在合成数据上，VCDF使VAR-LiNGAM的window/summary F1平均提升约0.08–0.12，且对中长序列收益更明显，长度≥1000时最高可达0.18的绝对提升。在模拟fMRI与IT监控等更贴近真实噪声场景中，也表现出更高的结构准确性与稳定性，证明其能有效提升时间序列因果发现结果的可靠性。

**关键词**：鲁棒性增强, 因果关系稳定性, 非平稳性, 采样变异, 噪声鲁棒性, 分块时间窗口, 共识验证框架, IT监控时序

**评分**：19

**论文链接**：[查看原文](https://arxiv.org/abs/2602.21381v1) | [下载PDF](https://arxiv.org/pdf/2602.21381v1.pdf)

---

## [11. Stable Deep Reinforcement Learning via Isotropic Gaussian Representations](https://arxiv.org/abs/2602.19373v1)

**作者**：Ali Saheb, Johan Obando-Ceron, Aaron Courville 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-22

### 📄 论文摘要

Deep reinforcement learning systems often suffer from unstable training dynamics due to non-stationarity, where learning objectives and data distributions evolve over time. We show that under non-stationary targets, isotropic Gaussian embeddings are provably advantageous. In particular, they induce stable tracking of time-varying targets for linear readouts, achieve maximal entropy under a fixed variance budget, and encourage a balanced use of all representational dimensions--all of which enable agents to be more adaptive and stable. Building on this insight, we propose the use of Sketched Isotropic Gaussian Regularization for shaping representations toward an isotropic Gaussian distribution during training. We demonstrate empirically, over a variety of domains, that this simple and computationally inexpensive method improves performance under non-stationarity while reducing representation collapse, neuron dormancy, and training instability.

### 🤖 AI 总结

**一句话总结**：论文提出用“各向同性高斯”约束来塑造深度强化学习表征，在非平稳目标下显著提升训练稳定性并减少表征退化。

**研究动机**：深度强化学习在训练过程中目标与数据分布不断变化（非平稳），易导致表示坍塌、神经元休眠与性能震荡。作者希望找到一种简单、低开销且有理论支撑的表征正则，以增强对时变目标的适应与稳定跟踪。

**核心方法**：从理论上说明在非平稳目标下，各向同性高斯嵌入对线性读出具有更稳定的时变目标跟踪性质，并在固定方差预算下实现最大熵、促进各维度均衡使用。基于此提出 Sketched Isotropic Gaussian Regularization（草图式各向同性高斯正则），在训练中将表示分布拉向各向同性高斯且计算开销较低。

**主要结论**：在多种任务域的实验中，该正则在非平稳环境下提升性能并降低训练不稳定。方法还能缓解表示坍塌与神经元休眠，使表征更均衡、适应性更强。

**关键词**：深度强化学习, 非平稳学习, 训练稳定性, 各向同性高斯表示, 高斯嵌入, 各向同性高斯正则化, 最大熵表示, 表征塌缩, 神经元休眠

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.19373v1) | [下载PDF](https://arxiv.org/pdf/2602.19373v1.pdf)

---

## [12. Golden Layers and Where to Find Them: Improved Knowledge Editing for Large Language Models Via Layer Gradient Analysis](https://arxiv.org/abs/2602.20207v1)

**作者**：Shrestha Datta, Hongfu Liu, Anshuman Chhabra  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-22

### 📄 论文摘要

Knowledge editing in Large Language Models (LLMs) aims to update the model's prediction for a specific query to a desired target while preserving its behavior on all other inputs. This process typically involves two stages: identifying the layer to edit and performing the parameter update. Intuitively, different queries may localize knowledge at different depths of the model, resulting in different sample-wise editing performance for a fixed editing layer. In this work, we hypothesize the existence of fixed golden layers that can achieve near-optimal editing performance similar to sample-wise optimal layers. To validate this hypothesis, we provide empirical evidence by comparing golden layers against ground-truth sample-wise optimal layers. Furthermore, we show that golden layers can be reliably identified using a proxy dataset and generalize effectively to unseen test set queries across datasets. Finally, we propose a novel method, namely Layer Gradient Analysis (LGA) that estimates golden layers efficiently via gradient-attribution, avoiding extensive trial-and-error across multiple editing runs. Extensive experiments on several benchmark datasets demonstrate the effectiveness and robustness of our LGA approach across different LLM types and various knowledge editing methods.

### 🤖 AI 总结

**一句话总结**：本研究提出了一种通过层梯度分析有效识别和利用固定的黄金层来改进大型语言模型的知识编辑方法。

**研究动机**：研究旨在提高大型语言模型在特定查询的知识更新能力，同时保持对其他输入的行为不变。

**核心方法**：提出了一种新的层梯度分析方法，通过梯度归因高效识别黄金层，避免多次编辑实验的试错过程。

**主要结论**：实验结果验证了黄金层的有效性和鲁棒性，并证明了该方法在不同类型的大型语言模型及各种知识编辑方法中的适用性。

**关键词**：知识编辑, LLM, 层梯度分析, 黄金层, 参数更新, 样本优化, 数据集泛化, 实验评估

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2602.20207v1) | [下载PDF](https://arxiv.org/pdf/2602.20207v1.pdf)

---

## [13. LLMs Can Learn to Reason Via Off-Policy RL](https://arxiv.org/abs/2602.19362v1)

**作者**：Daniel Ritter, Owen Oertell, Bradley Guo 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-22

### 📄 论文摘要

Reinforcement learning (RL) approaches for Large Language Models (LLMs) frequently use on-policy algorithms, such as PPO or GRPO. However, policy lag from distributed training architectures and differences between the training and inference policies break this assumption, making the data off-policy by design. To rectify this, prior work has focused on making this off-policy data appear more on-policy, either via importance sampling (IS), or by more closely aligning the training and inference policies by explicitly modifying the inference engine. In this work, we embrace off-policyness and propose a novel off-policy RL algorithm that does not require these modifications: Optimal Advantage-based Policy Optimization with Lagged Inference policy (OAPL). We show that OAPL outperforms GRPO with importance sampling on competition math benchmarks, and can match the performance of a publicly available coding model, DeepCoder, on LiveCodeBench, while using 3x fewer generations during training. We further empirically demonstrate that models trained via OAPL have improved test time scaling under the Pass@k metric. OAPL allows for efficient, effective post-training even with lags of more than 400 gradient steps between the training and inference policies, 100x more off-policy than prior approaches.

### 🤖 AI 总结

**一句话总结**：提出并验证一种适用于LLM分布式训练中天然离策略数据的离策略RL算法OAPL，在数学与代码基准上优于/可匹敌现有方法且训练更高效。

**研究动机**：LLM后训练常用PPO/GRPO等on-policy算法，但分布式训练带来的policy lag及训练/推理策略不一致使数据“设计上就离策略”，传统用IS或改推理引擎来“伪装成on-policy”成本高且受限。

**核心方法**：提出Optimal Advantage-based Policy Optimization with Lagged Inference policy（OAPL），直接在存在显著滞后（训练与推理策略相隔数百步）条件下进行稳定的优势驱动策略优化，无需重要性采样或改动推理系统。

**主要结论**：OAPL在竞赛数学基准上超过带IS的GRPO，在LiveCodeBench上以约3倍更少生成次数达到可与DeepCoder匹敌的表现，并提升Pass@k下的测试时扩展性；即使滞后超过400个梯度步、比以往方法更“离策略”约100倍仍能有效训练。

**关键词**：LLM强化学习, 离策略强化学习, 策略滞后, 分布式训练, 重要性采样, 优势函数优化, 策略优化算法, 后训练, 测试时扩展, 代码生成评测

**评分**：36

**论文链接**：[查看原文](https://arxiv.org/abs/2602.19362v1) | [下载PDF](https://arxiv.org/pdf/2602.19362v1.pdf)

---

## [14. Active perception and disentangled representations allow continual, episodic zero and few-shot learning](https://arxiv.org/abs/2602.19355v1)

**作者**：David Rawlinson, Gideon Kowadlo  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-22

### 📄 论文摘要

Generalization is often regarded as an essential property of machine learning systems. However, perhaps not every component of a system needs to generalize. Training models for generalization typically produces entangled representations at the boundaries of entities or classes, which can lead to destructive interference when rapid, high-magnitude updates are required for continual or few-shot learning. Techniques for fast learning with non-interfering representations exist, but they generally fail to generalize. Here, we describe a Complementary Learning System (CLS) in which the fast learner entirely foregoes generalization in exchange for continual zero-shot and few-shot learning. Unlike most CLS approaches, which use episodic memory primarily for replay and consolidation, our fast, disentangled learner operates as a parallel reasoning system. The fast learner can overcome observation variability and uncertainty by leveraging a conventional slow, statistical learner within an active perception system: A contextual bias provided by the fast learner induces the slow learner to encode novel stimuli in familiar, generalized terms, enabling zero-shot and few-shot learning. This architecture demonstrates that fast, context-driven reasoning can coexist with slow, structured generalization, providing a pathway for robust continual learning.

### 🤖 AI 总结

**一句话总结**：提出一种结合主动感知的互补学习系统（CLS）：让“快速学习器”放弃泛化、专注于去纠缠的情景推理，并借助“慢速学习器”的统计泛化来实现持续的零样本与小样本学习。

**研究动机**：追求强泛化往往会在类别边界形成纠缠表征，导致在持续学习或小样本学习所需的快速大幅更新时发生灾难性干扰；而现有不干扰的快速学习方法又常缺乏泛化能力。

**核心方法**：构建并行的快慢双系统：快学习器用去纠缠表征进行情景驱动的快速推理（不追求泛化），并在主动感知框架中提供上下文偏置，引导慢学习器用已学到的泛化概念对新刺激进行编码，从而在观测噪声/不确定性下实现零/小样本识别与学习。

**主要结论**：通过让快速系统专注于不干扰的情景推理、慢速系统专注于结构化泛化，并用主动感知把两者耦合，可在同一架构中同时获得鲁棒的持续学习能力与零/小样本学习表现。

**关键词**：持续学习, 零样本学习, 小样本学习, 互补学习系统（CLS）, 情景记忆, 解耦表示, 表征纠缠, 灾难性干扰, 主动感知, 快慢学习器, 上下文偏置

**评分**：26

**论文链接**：[查看原文](https://arxiv.org/abs/2602.19355v1) | [下载PDF](https://arxiv.org/pdf/2602.19355v1.pdf)

---

## [15. Smooth Gate Functions for Soft Advantage Policy Optimization](https://arxiv.org/abs/2602.19345v1)

**作者**：Egor Denisov, Svetlana Glazyrina, Maksim Kryzhanovskiy 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-22

### 📄 论文摘要

Group Relative Policy Optimization (GRPO) has significantly advanced the training of large language models and enhanced their reasoning capabilities, while it remains susceptible to instability due to the use of hard clipping. Soft Adaptive Policy Optimization (SAPO) addresses this limitation by replacing clipping with a smooth sigmoid-based gate function, which leads to more stable updates. We have decided to push this theory further and investigate the impact of different gate functions on both training stability and final model performance. We formalize the key properties that admissible gates should satisfy and identify several families of such functions for empirical evaluation. This paper presents an analysis of our findings based on experiments conducted with the Qwen2.5-7B-Instruct model on mathematical reasoning tasks. These results provide practical guidance for designing smoother and more robust policy optimization objectives for large language model training.

### 🤖 AI 总结

**一句话总结**：本文系统比较不同“平滑门控函数”替代硬裁剪在优势策略优化中的效果，以提升大模型RL训练的稳定性与最终性能。

**研究动机**：GRPO等方法依赖硬clipping，容易造成训练不稳定；SAPO用sigmoid门控缓解但门控函数选择缺乏系统研究，因此需要探索更合适的平滑门控设计。

**核心方法**：形式化定义“可用门控函数”应满足的关键性质，并构造多类满足条件的门控函数族；在Qwen2.5-7B-Instruct的数学推理任务上进行对比实验，评估训练稳定性与最终表现。

**主要结论**：相较硬裁剪，合适的平滑门控可带来更稳定的策略更新，并在不牺牲甚至提升性能的情况下改进训练鲁棒性；论文给出门控函数设计的经验性指导。

**关键词**：策略优化目标, 软门控函数, 硬剪切替代, 训练稳定性, 优势函数估计, 大语言模型对齐训练, 数学推理评测, 鲁棒更新

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2602.19345v1) | [下载PDF](https://arxiv.org/pdf/2602.19345v1.pdf)

---

