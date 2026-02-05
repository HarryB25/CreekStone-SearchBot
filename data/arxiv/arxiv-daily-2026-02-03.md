# arXiv AI 论文日报 | 2026-02-03

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (11 篇)
- [cs.LG](#csLG) (14 篇)
- [cs.CL](#csCL) (2 篇)
- [cs.AI](#csAI) (3 篇)

---

## cs.AI

## [1. AutoFigure: Generating and Refining Publication-Ready Scientific Illustrations](https://arxiv.org/abs/2602.03828v1)

**作者**：Minjun Zhu, Zhen Lin, Yixuan Weng 等 9 位作者  
**分类**：cs.AI, cs.CL, cs.CV, cs.DL  
**发布时间**：2026-02-03

### 📄 论文摘要

High-quality scientific illustrations are crucial for effectively communicating complex scientific and technical concepts, yet their manual creation remains a well-recognized bottleneck in both academia and industry. We present FigureBench, the first large-scale benchmark for generating scientific illustrations from long-form scientific texts. It contains 3,300 high-quality scientific text-figure pairs, covering diverse text-to-illustration tasks from scientific papers, surveys, blogs, and textbooks. Moreover, we propose AutoFigure, the first agentic framework that automatically generates high-quality scientific illustrations based on long-form scientific text. Specifically, before rendering the final result, AutoFigure engages in extensive thinking, recombination, and validation to produce a layout that is both structurally sound and aesthetically refined, outputting a scientific illustration that achieves both structural completeness and aesthetic appeal. Leveraging the high-quality data from FigureBench, we conduct extensive experiments to test the performance of AutoFigure against various baseline methods. The results demonstrate that AutoFigure consistently surpasses all baseline methods, producing publication-ready scientific illustrations. The code, dataset and huggingface space are released in https://github.com/ResearAI/AutoFigure.

### 🤖 AI 总结

**一句话总结**：AutoFigure是一个自动生成高质量科学插图的框架，基于长文本输入，并通过FigureBench进行评估。

**研究动机**：科学插图在有效传达复杂概念方面至关重要，但手动制作过程效率低下，亟需自动化解决方案。

**核心方法**：AutoFigure框架通过思考、重组和验证，生成结构合理且美观的科学插图，同时依托FigureBench数据集进行性能评估。

**主要结论**：实验结果表明，AutoFigure在生成符合出版标准的科学插图方面性能优于所有基线方法。

**关键词**：生成, 科学插图, 自动生成, 机器学习, 深度学习, 神经网络, 代理框架, 文本到插图, FigureBench, 论文插图, agent

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2602.03828v1) | [下载PDF](https://arxiv.org/pdf/2602.03828v1.pdf)

---

## [2. Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity](https://arxiv.org/abs/2602.03794v1)

**作者**：Yingxuan Yang, Chengrui Qu, Muning Wen 等 8 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-02-03

### 📄 论文摘要

LLM-based multi-agent systems (MAS) have emerged as a promising approach to tackle complex tasks that are difficult for individual LLMs. A natural strategy is to scale performance by increasing the number of agents; however, we find that such scaling exhibits strong diminishing returns in homogeneous settings, while introducing heterogeneity (e.g., different models, prompts, or tools) continues to yield substantial gains. This raises a fundamental question: what limits scaling, and why does diversity help? We present an information-theoretic framework showing that MAS performance is bounded by the intrinsic task uncertainty, not by agent count. We derive architecture-agnostic bounds demonstrating that improvements depend on how many effective channels the system accesses. Homogeneous agents saturate early because their outputs are strongly correlated, whereas heterogeneous agents contribute complementary evidence. We further introduce $K^*$, an effective channel count that quantifies the number of effective channels without ground-truth labels. Empirically, we show that heterogeneous configurations consistently outperform homogeneous scaling: 2 diverse agents can match or exceed the performance of 16 homogeneous agents. Our results provide principled guidelines for building efficient and robust MAS through diversity-aware design. Code and Dataset are available at the link: https://github.com/SafeRL-Lab/Agent-Scaling.

### 🤖 AI 总结

**一句话总结**：异构多智能体系统在性能扩展上优于同质智能体系统，因为多样性显著提升了任务处理能力。

**研究动机**：研究者希望理解在基于LLM的多智能体系统中，智能体数量增加时为何存在边际效益递减现象，以及多样性如何提升性能。

**核心方法**：通过信息论框架，提出了有效通道数K*的概念，以量化不同配置的贡献，并分析任务不确定性对性能的限制。

**主要结论**：异构智能体配置的性能一致超越同质智能体，提供了通过多样性设计构建高效、稳健的多智能体系统的指导。

**关键词**：多代理系统, LLM, 代理, 多样性, 任务不确定性, 信息论框架, 效果通道, 协同工作, 机器学习, 深度学习

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2602.03794v1) | [下载PDF](https://arxiv.org/pdf/2602.03794v1.pdf)

---

## [3. AOrchestra: Automating Sub-Agent Creation for Agentic Orchestration](https://arxiv.org/abs/2602.03786v1)

**作者**：Jianhao Ruan, Zhihao Xu, Yiran Peng 等 11 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-02-03

### 📄 论文摘要

Language agents have shown strong promise for task automation. Realizing this promise for increasingly complex, long-horizon tasks has driven the rise of a sub-agent-as-tools paradigm for multi-turn task solving. However, existing designs still lack a dynamic abstraction view of sub-agents, thereby hurting adaptability. We address this challenge with a unified, framework-agnostic agent abstraction that models any agent as a tuple Instruction, Context, Tools, Model. This tuple acts as a compositional recipe for capabilities, enabling the system to spawn specialized executors for each task on demand. Building on this abstraction, we introduce an agentic system AOrchestra, where the central orchestrator concretizes the tuple at each step: it curates task-relevant context, selects tools and models, and delegates execution via on-the-fly automatic agent creation. Such designs enable reducing human engineering efforts, and remain framework-agnostic with plug-and-play support for diverse agents as task executors. It also enables a controllable performance-cost trade-off, allowing the system to approach Pareto-efficient. Across three challenging benchmarks (GAIA, SWE-Bench, Terminal-Bench), AOrchestra achieves 16.28% relative improvement against the strongest baseline when paired with Gemini-3-Flash. The code is available at: https://github.com/FoundationAgents/AOrchestra

### 🤖 AI 总结

**一句话总结**：AOrchestra是一个自动化子代理创建的系统，通过动态抽象模型提升多轮任务解决的适应性和效率。

**研究动机**：现有的子代理设计缺乏动态抽象视图，限制了其适应性，迫切需要一种能够自动创建和管理子代理的系统。

**核心方法**：AOrchestra采用统一的代理抽象模型，将代理表示为指令、上下文、工具和模型的元组，以便动态生成专用执行器。

**主要结论**：在GAIA、SWE-Bench和Terminal-Bench等三个基准测试中，AOrchestra相较于最强基准实现了16.28%的相对提升，展示了其在任务执行中的有效性。

**关键词**：子代理, 任务自动化, 多轮任务解决, 代理抽象, 统一框架, 自适应能力, AOrchestra, 任务执行器, 代理系统, 绩效成本权衡, agent

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2602.03786v1) | [下载PDF](https://arxiv.org/pdf/2602.03786v1.pdf)

---

## cs.CL

## [4. Accelerating Scientific Research with Gemini: Case Studies and Common Techniques](https://arxiv.org/abs/2602.03837v1)

**作者**：David P. Woodruff, Vincent Cohen-Addad, Lalit Jain 等 34 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-02-03

### 📄 论文摘要

Recent advances in large language models (LLMs) have opened new avenues for accelerating scientific research. While models are increasingly capable of assisting with routine tasks, their ability to contribute to novel, expert-level mathematical discovery is less understood. We present a collection of case studies demonstrating how researchers have successfully collaborated with advanced AI models, specifically Google's Gemini-based models (in particular Gemini Deep Think and its advanced variants), to solve open problems, refute conjectures, and generate new proofs across diverse areas in theoretical computer science, as well as other areas such as economics, optimization, and physics. Based on these experiences, we extract common techniques for effective human-AI collaboration in theoretical research, such as iterative refinement, problem decomposition, and cross-disciplinary knowledge transfer. While the majority of our results stem from this interactive, conversational methodology, we also highlight specific instances that push beyond standard chat interfaces. These include deploying the model as a rigorous adversarial reviewer to detect subtle flaws in existing proofs, and embedding it within a "neuro-symbolic" loop that autonomously writes and executes code to verify complex derivations. Together, these examples highlight the potential of AI not just as a tool for automation, but as a versatile, genuine partner in the creative process of scientific discovery.

### 🤖 AI 总结

**一句话总结**：本论文展示了如何利用Gemini模型加速科学研究，并提炼出有效的人机协作技术。

**研究动机**：随着大语言模型的发展，探索其在高水平数学发现中的应用潜力成为研究的动机。

**核心方法**：通过案例研究，展示了Gemini模型在解决开放问题和生成新证明中的应用，并总结了迭代优化、问题分解等协作技术。

**主要结论**：AI不仅可以作为自动化工具，还能作为科学发现过程中的创新合作伙伴，推动研究进展。

**关键词**：机器学习, 深度学习, 神经网络, 大语言模型, 人机协作, 迭代优化, 跨学科知识转移, 生成模型, 自主代码执行, llm

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2602.03837v1) | [下载PDF](https://arxiv.org/pdf/2602.03837v1.pdf)

---

## [5. They Said Memes Were Harmless-We Found the Ones That Hurt: Decoding Jokes, Symbols, and Cultural References](https://arxiv.org/abs/2602.03822v1)

**作者**：Sahil Tripathi, Gautam Siddharth Kashyap, Mehwish Nasim 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-02-03

### 📄 论文摘要

Meme-based social abuse detection is challenging because harmful intent often relies on implicit cultural symbolism and subtle cross-modal incongruence. Prior approaches, from fusion-based methods to in-context learning with Large Vision-Language Models (LVLMs), have made progress but remain limited by three factors: i) cultural blindness (missing symbolic context), ii) boundary ambiguity (satire vs. abuse confusion), and iii) lack of interpretability (opaque model reasoning). We introduce CROSS-ALIGN+, a three-stage framework that systematically addresses these limitations: (1) Stage I mitigates cultural blindness by enriching multimodal representations with structured knowledge from ConceptNet, Wikidata, and Hatebase; (2) Stage II reduces boundary ambiguity through parameter-efficient LoRA adapters that sharpen decision boundaries; and (3) Stage III enhances interpretability by generating cascaded explanations. Extensive experiments on five benchmarks and eight LVLMs demonstrate that CROSS-ALIGN+ consistently outperforms state-of-the-art methods, achieving up to 17% relative F1 improvement while providing interpretable justifications for each decision.

### 🤖 AI 总结

**一句话总结**：CROSS-ALIGN+是一个三阶段框架，旨在提高基于表情包的社会虐待检测的效果，克服文化盲点、边界模糊和缺乏可解释性的问题。

**研究动机**：表情包中的社会虐待检测面临挑战，因为有害意图常常依赖于隐含的文化符号和微妙的跨模态不一致性。

**核心方法**：CROSS-ALIGN+通过三个阶段依次解决文化盲点、边界模糊和可解释性问题，利用知识库丰富多模态表示，优化决策边界，并生成级联解释。

**主要结论**：实验结果表明，CROSS-ALIGN+在五个基准和八个大型视觉语言模型上均优于现有方法，最高可实现17%的相对F1提升，并提供可解释的决策依据。

**关键词**：关键词：深度学习, 大规模视觉语言模型, 文化符号, 多模态表示, 解释性, CROSS-ALIGN+, 参数高效, 决策边界, 语义搜索, ml

**评分**：68

**论文链接**：[查看原文](https://arxiv.org/abs/2602.03822v1) | [下载PDF](https://arxiv.org/pdf/2602.03822v1.pdf)

---

## cs.CV

## [6. EventNeuS: 3D Mesh Reconstruction from a Single Event Camera](https://arxiv.org/abs/2602.03847v1)

**作者**：Shreyas Sachan, Viktor Rudnev, Mohamed Elgharib 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-03

### 📄 论文摘要

Event cameras offer a considerable alternative to RGB cameras in many scenarios. While there are recent works on event-based novel-view synthesis, dense 3D mesh reconstruction remains scarcely explored and existing event-based techniques are severely limited in their 3D reconstruction accuracy. To address this limitation, we present EventNeuS, a self-supervised neural model for learning 3D representations from monocular colour event streams. Our approach, for the first time, combines 3D signed distance function and density field learning with event-based supervision. Furthermore, we introduce spherical harmonics encodings into our model for enhanced handling of view-dependent effects. EventNeuS outperforms existing approaches by a significant margin, achieving 34% lower Chamfer distance and 31% lower mean absolute error on average compared to the best previous method.

### 🤖 AI 总结

**一句话总结**：EventNeuS是一种自监督神经模型，通过单一事件相机的彩色事件流学习3D表示，显著提高了3D网格重建的准确性。

**研究动机**：尽管近期在基于事件的视图合成方面取得了一定进展，但密集的3D网格重建仍然缺乏深入研究，现有技术在3D重建精度上存在严重局限。

**核心方法**：EventNeuS首次结合了3D符号距离函数和密度场学习，并引入球谐编码以增强对视角依赖效应的处理能力。

**主要结论**：EventNeuS在性能上显著优于现有方法，平均实现了34%的Chamfer距离降低和31%的平均绝对误差降低。

**关键词**：3D重建, 事件相机, 自监督, 神经网络, 视图依赖效果, 事件驱动, 生成模型, 模型优化, 语义搜索, rag

**评分**：71

**论文链接**：[查看原文](https://arxiv.org/abs/2602.03847v1) | [下载PDF](https://arxiv.org/pdf/2602.03847v1.pdf)

---

## [7. Continuous Control of Editing Models via Adaptive-Origin Guidance](https://arxiv.org/abs/2602.03826v1)

**作者**：Alon Wolf, Chen Katzir, Kfir Aberman 等 4 位作者  
**分类**：cs.CV, cs.GR  
**发布时间**：2026-02-03

### 📄 论文摘要

Diffusion-based editing models have emerged as a powerful tool for semantic image and video manipulation. However, existing models lack a mechanism for smoothly controlling the intensity of text-guided edits. In standard text-conditioned generation, Classifier-Free Guidance (CFG) impacts prompt adherence, suggesting it as a potential control for edit intensity in editing models. However, we show that scaling CFG in these models does not produce a smooth transition between the input and the edited result. We attribute this behavior to the unconditional prediction, which serves as the guidance origin and dominates the generation at low guidance scales, while representing an arbitrary manipulation of the input content. To enable continuous control, we introduce Adaptive-Origin Guidance (AdaOr), a method that adjusts this standard guidance origin with an identity-conditioned adaptive origin, using an identity instruction corresponding to the identity manipulation. By interpolating this identity prediction with the standard unconditional prediction according to the edit strength, we ensure a continuous transition from the input to the edited result. We evaluate our method on image and video editing tasks, demonstrating that it provides smoother and more consistent control compared to current slider-based editing approaches. Our method incorporates an identity instruction into the standard training framework, enabling fine-grained control at inference time without per-edit procedure or reliance on specialized datasets.

### 🤖 AI 总结

**一句话总结**：本论文提出了一种自适应引导方法AdaOr，旨在实现对编辑模型的平滑控制，从而改善文本引导编辑的强度调节。

**研究动机**：现有的扩散编辑模型在文本引导编辑的强度控制上存在不足，难以实现输入与编辑结果之间的平滑过渡。

**核心方法**：提出的AdaOr方法通过将标准无条件预测与身份条件自适应预测进行插值，根据编辑强度调整引导原点，实现连续控制。

**主要结论**：与现有基于滑块的编辑方法相比，AdaOr在图像和视频编辑任务中提供了更平滑、更一致的控制，且无需依赖特定数据集或逐个编辑过程。

**关键词**：扩散模型, 编辑模型, 语义图像, 视频操控, 自适应引导, 生成模型, 控制强度, 细粒度控制, 机器学习, 深度学习, diffusion

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2602.03826v1) | [下载PDF](https://arxiv.org/pdf/2602.03826v1.pdf)

---

## [8. From Pre- to Intra-operative MRI: Predicting Brain Shift in Temporal Lobe Resection for Epilepsy Surgery](https://arxiv.org/abs/2602.03785v1)

**作者**：Jingjing Peng, Giorgio Fiore, Yang Liu 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-03

### 📄 论文摘要

Introduction: In neurosurgery, image-guided Neurosurgery Systems (IGNS) highly rely on preoperative brain magnetic resonance images (MRI) to assist surgeons in locating surgical targets and determining surgical paths. However, brain shift invalidates the preoperative MRI after dural opening. Updated intraoperative brain MRI with brain shift compensation is crucial for enhancing the precision of neuronavigation systems and ensuring the optimal outcome of surgical interventions. Methodology: We propose NeuralShift, a U-Net-based model that predicts brain shift entirely from pre-operative MRI for patients undergoing temporal lobe resection. We evaluated our results using Target Registration Errors (TREs) computed on anatomical landmarks located on the resection side and along the midline, and DICE scores comparing predicted intraoperative masks with masks derived from intraoperative MRI. Results: Our experimental results show that our model can predict the global deformation of the brain (DICE of 0.97) with accurate local displacements (achieve landmark TRE as low as 1.12 mm), compensating for large brain shifts during temporal lobe removal neurosurgery. Conclusion: Our proposed model is capable of predicting the global deformation of the brain during temporal lobe resection using only preoperative images, providing potential opportunities to the surgical team to increase safety and efficiency of neurosurgery and better outcomes to patients. Our contributions will be publicly available after acceptance in https://github.com/SurgicalDataScienceKCL/NeuralShift.

### 🤖 AI 总结

**一句话总结**：本文提出了一种基于U-Net的模型NeuralShift，能够仅通过术前MRI预测癫痫手术中的脑位移。

**研究动机**：在神经外科中，术前MRI受到脑位移的影响，导致定位不准确，因此需要更新的术中MRI来补偿脑位移。

**核心方法**：我们提出的NeuralShift模型利用术前MRI数据，预测癫痫手术中脑的全球变形，并通过目标注册误差和DICE分数评估模型性能。

**主要结论**：该模型能够有效预测脑位移，从而提高神经外科手术的安全性和效率，改善患者的手术结果。

**关键词**：神经网络, 深度学习, 预测模型, U-Net, 神经外科, 脑移位, 图像引导, 手术导航, DICE评分, 目标注册误差, agent

**评分**：68

**论文链接**：[查看原文](https://arxiv.org/abs/2602.03785v1) | [下载PDF](https://arxiv.org/pdf/2602.03785v1.pdf)

---

## [9. QVLA: Not All Channels Are Equal in Vision-Language-Action Model's Quantization](https://arxiv.org/abs/2602.03782v1)

**作者**：Yuhao Xu, Yantai Yang, Zhenyang Fan 等 7 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-02-03

### 📄 论文摘要

The advent of Vision-Language-Action (VLA) models represents a significant leap for embodied intelligence, yet their immense computational demands critically hinder deployment on resource-constrained robotic platforms. Intuitively, low-bit quantization is a prevalent and preferred technique for large-scale model compression. However, we find that a systematic analysis of VLA model's quantization is fundamentally lacking. We argue that naively applying uniform-bit quantization from Large Language Models (LLMs) to robotics is flawed, as these methods prioritize passive data fidelity while ignoring how minor action deviations compound into catastrophic task failures. To bridge this gap, we introduce QVLA, the first action-centric quantization framework specifically designed for embodied control. In a sharp departure from the rigid, uniform-bit quantization of LLM-based methods, QVLA introduces a highly granular, channel-wise bit allocation strategy. Its core mechanism is to directly measure the final action-space sensitivity when quantizing each individual channel to various bit-widths. This process yields a precise, per-channel importance metric that guides a global optimization, which elegantly unifies quantization and pruning (0-bit) into a single, cohesive framework. Extensive evaluations on different baselines demonstrate the superiority of our approach. In the LIBERO, the quantization version of OpenVLA-OFT with our method requires only 29.2% of the original model's VRAM while maintaining 98.9% of its original performance and achieving a 1.49x speedup. This translates to a 22.6% performance improvement over the LLM-derived method SmoothQuant. Our work establishes a new, principled foundation for compressing VLA models in robotics, paving the way for deploying powerful, large-scale models on real-world hardware. Code will be released.

### 🤖 AI 总结

**一句话总结**：QVLA是一种针对视觉-语言-动作模型量化的新框架，采用通道级比特分配策略，显著提升了模型压缩效果和性能。

**研究动机**：现有的统一比特量化方法在机器人领域的应用存在缺陷，无法有效处理动作偏差对任务失败的影响，因此需要一个更为精细的量化策略。

**核心方法**：QVLA框架通过直接测量每个通道在不同比特宽度下的最终动作空间敏感性，提供了通道重要性度量，并将量化与剪枝统一为一个优化框架。

**主要结论**：QVLA在LIBERO数据集上的实验表明，其量化版本仅需29.2%的原始模型显存，同时保持98.9%的原始性能，实现了1.49倍的加速，显著优于传统方法。

**关键词**：量子化, 视觉-语言-动作, embodied intelligence, 低比特量子化, 模型压缩, QVLA, 机器人控制, action-centric quantization, channel-wise bit allocation, 性能提升, llm

**评分**：68

**论文链接**：[查看原文](https://arxiv.org/abs/2602.03782v1) | [下载PDF](https://arxiv.org/pdf/2602.03782v1.pdf)

---

## [10. FOVI: A biologically-inspired foveated interface for deep vision models](https://arxiv.org/abs/2602.03766v1)

**作者**：Nicholas M. Blauch, George A. Alvarez, Talia Konkle  
**分类**：cs.CV, cs.NE, q-bio.NC  
**发布时间**：2026-02-03

### 📄 论文摘要

Human vision is foveated, with variable resolution peaking at the center of a large field of view; this reflects an efficient trade-off for active sensing, allowing eye-movements to bring different parts of the world into focus with other parts of the world in context. In contrast, most computer vision systems encode the visual world at a uniform resolution, raising challenges for processing full-field high-resolution images efficiently. We propose a foveated vision interface (FOVI) based on the human retina and primary visual cortex, that reformats a variable-resolution retina-like sensor array into a uniformly dense, V1-like sensor manifold. Receptive fields are defined as k-nearest-neighborhoods (kNNs) on the sensor manifold, enabling kNN-convolution via a novel kernel mapping technique. We demonstrate two use cases: (1) an end-to-end kNN-convolutional architecture, and (2) a foveated adaptation of the foundational DINOv3 ViT model, leveraging low-rank adaptation (LoRA). These models provide competitive performance at a fraction of the computational cost of non-foveated baselines, opening pathways for efficient and scalable active sensing for high-resolution egocentric vision. Code and pre-trained models are available at https://github.com/nblauch/fovi and https://huggingface.co/fovi-pytorch.

### 🤖 AI 总结

**一句话总结**：FOVI是一种受生物启发的凹视界面，通过模拟人类视网膜提高深度视觉模型的效率和性能。

**研究动机**：人类的视力具有可变分辨率的特性，而大多数计算机视觉系统却使用均匀分辨率，这导致处理高分辨率图像时的效率问题。

**核心方法**：FOVI通过将可变分辨率的传感器阵列重塑为均匀密集的传感器流形，并定义接收场为k近邻，利用新颖的核映射技术实现kNN卷积。

**主要结论**：FOVI在计算成本上显著优于非凹视模型，展示了高效、可扩展的主动感知在高分辨率自我中心视觉中的应用潜力。

**关键词**：生物启发, foveated interface, 深度视觉模型, 视觉处理, kNN卷积, DINOv3, 低秩适应, 主动感知, 计算效率, ml

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.03766v1) | [下载PDF](https://arxiv.org/pdf/2602.03766v1.pdf)

---

## [11. RAWDet-7: A Multi-Scenario Benchmark for Object Detection and Description on Quantized RAW Images](https://arxiv.org/abs/2602.03760v1)

**作者**：Mishal Fatima, Shashank Agnihotri, Kanchana Vaishnavi Gandikota 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-03

### 📄 论文摘要

Most vision models are trained on RGB images processed through ISP pipelines optimized for human perception, which can discard sensor-level information useful for machine reasoning. RAW images preserve unprocessed scene data, enabling models to leverage richer cues for both object detection and object description, capturing fine-grained details, spatial relationships, and contextual information often lost in processed images. To support research in this domain, we introduce RAWDet-7, a large-scale dataset of ~25k training and 7.6k test RAW images collected across diverse cameras, lighting conditions, and environments, densely annotated for seven object categories following MS-COCO and LVIS conventions. In addition, we provide object-level descriptions derived from the corresponding high-resolution sRGB images, facilitating the study of object-level information preservation under RAW image processing and low-bit quantization. The dataset allows evaluation under simulated 4-bit, 6-bit, and 8-bit quantization, reflecting realistic sensor constraints, and provides a benchmark for studying detection performance, description quality & detail, and generalization in low-bit RAW image processing. Dataset & code upon acceptance.

### 🤖 AI 总结

**一句话总结**：RAWDet-7是一个用于量化RAW图像下物体检测和描述的大型数据集，包含25k训练和7.6k测试图像。

**研究动机**：现有视觉模型多基于RGB图像，忽视了RAW图像中保留的传感器级信息，这些信息对机器推理有重要价值。

**核心方法**：构建了一个包含多种相机和环境的RAW图像数据集，并提供了多种量化模拟以评估物体检测和描述性能。

**主要结论**：RAWDet-7为研究量化RAW图像处理下的物体检测和描述提供了基准，显示了在低位数情况下的信息保留能力。

**关键词**：目标检测, RAW图像, 机器学习, 深度学习, 数据集, 计算机视觉, 语义搜索, 多场景基准, 低位量化, 物体描述, rag

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2602.03760v1) | [下载PDF](https://arxiv.org/pdf/2602.03760v1.pdf)

---

## [12. Zero-shot large vision-language model prompting for automated bone identification in paleoradiology x-ray archives](https://arxiv.org/abs/2602.03750v1)

**作者**：Owen Dong, Lily Gao, Manish Kota 等 7 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-02-03

### 📄 论文摘要

Paleoradiology, the use of modern imaging technologies to study archaeological and anthropological remains, offers new windows on millennial scale patterns of human health. Unfortunately, the radiographs collected during field campaigns are heterogeneous: bones are disarticulated, positioning is ad hoc, and laterality markers are often absent. Additionally, factors such as age at death, age of bone, sex, and imaging equipment introduce high variability. Thus, content navigation, such as identifying a subset of images with a specific projection view, can be time consuming and difficult, making efficient triaging a bottleneck for expert analysis. We report a zero shot prompting strategy that leverages a state of the art Large Vision Language Model (LVLM) to automatically identify the main bone, projection view, and laterality in such images. Our pipeline converts raw DICOM files to bone windowed PNGs, submits them to the LVLM with a carefully engineered prompt, and receives structured JSON outputs, which are extracted and formatted onto a spreadsheet in preparation for validation. On a random sample of 100 images reviewed by an expert board certified paleoradiologist, the system achieved 92% main bone accuracy, 80% projection view accuracy, and 100% laterality accuracy, with low or medium confidence flags for ambiguous cases. These results suggest that LVLMs can substantially accelerate code word development for large paleoradiology datasets, allowing for efficient content navigation in future anthropology workflows.

### 🤖 AI 总结

**一句话总结**：该研究提出了一种零-shot提示策略，利用大型视觉语言模型自动识别古人类放射学X光图像中的主要骨骼、投影视图和侧向性。

**研究动机**：古人类放射学中的X光图像数据异质性使得专家分析效率低下，因此需要一种自动化的方法来加速图像内容的导航和分类。

**核心方法**：研究中使用了先进的大型视觉语言模型，通过精心设计的提示将原始DICOM文件转换为骨窗PNG格式，并输出结构化的JSON数据。

**主要结论**：实验结果表明，该系统在骨骼识别、投影视图和侧向性识别上取得了高准确率，显示了大型视觉语言模型在古人类放射学数据集中的潜在应用价值。

**关键词**：大模型, 视觉语言模型, 自动化识别, 骨骼识别, 影像分析, DICOM处理, 人机协作, 专家验证, 内容导航, rag

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2602.03750v1) | [下载PDF](https://arxiv.org/pdf/2602.03750v1.pdf)

---

## [13. See-through: Single-image Layer Decomposition for Anime Characters](https://arxiv.org/abs/2602.03749v1)

**作者**：Jian Lin, Chengze Li, Haoyun Qin 等 8 位作者  
**分类**：cs.CV, cs.GR  
**发布时间**：2026-02-03

### 📄 论文摘要

We introduce a framework that automates the transformation of static anime illustrations into manipulatable 2.5D models. Current professional workflows require tedious manual segmentation and the artistic ``hallucination'' of occluded regions to enable motion. Our approach overcomes this by decomposing a single image into fully inpainted, semantically distinct layers with inferred drawing orders. To address the scarcity of training data, we introduce a scalable engine that bootstraps high-quality supervision from commercial Live2D models, capturing pixel-perfect semantics and hidden geometry. Our methodology couples a diffusion-based Body Part Consistency Module, which enforces global geometric coherence, with a pixel-level pseudo-depth inference mechanism. This combination resolves the intricate stratification of anime characters, e.g., interleaving hair strands, allowing for dynamic layer reconstruction. We demonstrate that our approach yields high-fidelity, manipulatable models suitable for professional, real-time animation applications.

### 🤖 AI 总结

**一句话总结**：本研究提出了一种框架，将静态动漫插图自动转换为可操作的2.5D模型，通过单图层分解实现高质量动画效果。

**研究动机**：当前专业工作流程需要繁琐的手动分割和艺术性补全，限制了动漫角色的动态表现能力，因此需要一种自动化的方法来提升效率。

**核心方法**：本方法通过将单幅图像分解为语义明确的层，并使用基于扩散的身体部位一致性模块和伪深度推断机制，实现了动漫角色的动态层重构。

**主要结论**：实验表明，该方法能够生成高保真、可操作的模型，适用于专业实时动画应用。

**关键词**：单幅图像, 层分解, 动漫角色, 2.5D模型, 语义分层, 像素级推断, 生成模型, 深度学习, 语义一致性, diffusion

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2602.03749v1) | [下载PDF](https://arxiv.org/pdf/2602.03749v1.pdf)

---

## [14. LIVE: Long-horizon Interactive Video World Modeling](https://arxiv.org/abs/2602.03747v1)

**作者**：Junchao Huang, Ziyang Ye, Xinting Hu 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-03

### 📄 论文摘要

Autoregressive video world models predict future visual observations conditioned on actions. While effective over short horizons, these models often struggle with long-horizon generation, as small prediction errors accumulate over time. Prior methods alleviate this by introducing pre-trained teacher models and sequence-level distribution matching, which incur additional computational cost and fail to prevent error propagation beyond the training horizon. In this work, we propose LIVE, a Long-horizon Interactive Video world modEl that enforces bounded error accumulation via a novel cycle-consistency objective, thereby eliminating the need for teacher-based distillation. Specifically, LIVE first performs a forward rollout from ground-truth frames and then applies a reverse generation process to reconstruct the initial state. The diffusion loss is subsequently computed on the reconstructed terminal state, providing an explicit constraint on long-horizon error propagation. Moreover, we provide an unified view that encompasses different approaches and introduce progressive training curriculum to stabilize training. Experiments demonstrate that LIVE achieves state-of-the-art performance on long-horizon benchmarks, generating stable, high-quality videos far beyond training rollout lengths.

### 🤖 AI 总结

**一句话总结**：本文提出了一种新的视频世界建模方法LIVE，能够在长时间范围内有效预测视频，减少预测误差的累积。

**研究动机**：传统的自回归视频模型在长时间预测中表现不佳，导致误差累积和生成质量下降，因此需要一种新的方法来改善这一问题。

**核心方法**：LIVE通过引入循环一致性目标来限制误差累积，采用前向生成和反向重建的过程来提高长时间预测的稳定性与质量。

**主要结论**：实验表明，LIVE在长时间基准测试中表现优异，生成的视频质量高且稳定，超出训练范围的生成能力显著提升。

**关键词**：长视距, 交互式视频, 世界建模, 自回归模型, 循环一致性, 生成模型, 训练课程, 稳定性, 预测错误, 视觉观察, diffusion

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.03747v1) | [下载PDF](https://arxiv.org/pdf/2602.03747v1.pdf)

---

## [15. Edge-Optimized Vision-Language Models for Underground Infrastructure Assessment](https://arxiv.org/abs/2602.03742v1)

**作者**：Johny J. Lopez, Md Meftahul Ferdaus, Mahdi Abdelguerfi  
**分类**：cs.CV  
**发布时间**：2026-02-03

### 📄 论文摘要

Autonomous inspection of underground infrastructure, such as sewer and culvert systems, is critical to public safety and urban sustainability. Although robotic platforms equipped with visual sensors can efficiently detect structural deficiencies, the automated generation of human-readable summaries from these detections remains a significant challenge, especially on resource-constrained edge devices. This paper presents a novel two-stage pipeline for end-to-end summarization of underground deficiencies, combining our lightweight RAPID-SCAN segmentation model with a fine-tuned Vision-Language Model (VLM) deployed on an edge computing platform. The first stage employs RAPID-SCAN (Resource-Aware Pipeline Inspection and Defect Segmentation using Compact Adaptive Network), achieving 0.834 F1-score with only 0.64M parameters for efficient defect segmentation. The second stage utilizes a fine-tuned Phi-3.5 VLM that generates concise, domain-specific summaries in natural language from the segmentation outputs. We introduce a curated dataset of inspection images with manually verified descriptions for VLM fine-tuning and evaluation. To enable real-time performance, we employ post-training quantization with hardware-specific optimization, achieving significant reductions in model size and inference latency without compromising summarization quality. We deploy and evaluate our complete pipeline on a mobile robotic platform, demonstrating its effectiveness in real-world inspection scenarios. Our results show the potential of edge-deployable integrated AI systems to bridge the gap between automated defect detection and actionable insights for infrastructure maintenance, paving the way for more scalable and autonomous inspection solutions.

### 🤖 AI 总结

**一句话总结**：本研究提出了一种边缘优化的视觉语言模型，用于地下基础设施的自动检测和总结，提升了检测效率和实时性。

**研究动机**：地下基础设施的自动检测对公共安全和城市可持续发展至关重要，但在资源受限的边缘设备上生成可读的检测摘要仍然是一个挑战。

**核心方法**：本文提出了一个两阶段的管道，结合了轻量级的RAPID-SCAN分割模型和精调的视觉语言模型，在边缘计算平台上实现了高效的缺陷分割和摘要生成。

**主要结论**：该系统在移动机器人平台上进行了评估，展示了边缘可部署的集成AI系统在自动缺陷检测与基础设施维护洞察之间的桥梁作用，为更可扩展的自动检测解决方案铺平了道路。

**关键词**：视觉语言模型, 深度学习, 机器人平台, 自动化检测, 边缘计算, 资源感知, 缺陷分割, 实时性能, 模型优化, 自主检查, autonomous

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.03742v1) | [下载PDF](https://arxiv.org/pdf/2602.03742v1.pdf)

---

## [16. RegionReasoner: Region-Grounded Multi-Round Visual Reasoning](https://arxiv.org/abs/2602.03733v1)

**作者**：Wenfang Sun, Hao Chen, Yingjun Du 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-03

### 📄 论文摘要

Large vision-language models have achieved remarkable progress in visual reasoning, yet most existing systems rely on single-step or text-only reasoning, limiting their ability to iteratively refine understanding across multiple visual contexts. To address this limitation, we introduce a new multi-round visual reasoning benchmark with training and test sets spanning both detection and segmentation tasks, enabling systematic evaluation under iterative reasoning scenarios. We further propose RegionReasoner, a reinforcement learning framework that enforces grounded reasoning by requiring each reasoning trace to explicitly cite the corresponding reference bounding boxes, while maintaining semantic coherence via a global-local consistency reward. This reward extracts key objects and nouns from both global scene captions and region-level captions, aligning them with the reasoning trace to ensure consistency across reasoning steps. RegionReasoner is optimized with structured rewards combining grounding fidelity and global-local semantic alignment. Experiments on detection and segmentation tasks show that RegionReasoner-7B, together with our newly introduced benchmark RegionDial-Bench, considerably improves multi-round reasoning accuracy, spatial grounding precision, and global-local consistency, establishing a strong baseline for this emerging research direction.

### 🤖 AI 总结

**一句话总结**：RegionReasoner是一种通过多轮推理和强化学习框架提高视觉推理准确性的模型。

**研究动机**：现有的视觉语言模型在多轮推理方面能力有限，因此需要一种新的基准和方法来提升其在检测和分割任务中的表现。

**核心方法**：RegionReasoner通过要求每个推理过程明确引用对应的边界框，并结合全局-局部一致性奖励，优化推理的准确性和一致性。

**主要结论**：实验表明，RegionReasoner-7B显著提升了多轮推理的准确性和空间定位的精确度，为这一新兴研究方向奠定了坚实的基线。

**关键词**：视觉推理, 多轮推理, 强化学习, 语义一致性, RegionReasoner, 视觉-语言模型, 检测与分割, 奖励模型, 迭代推理, context

**评分**：73

**论文链接**：[查看原文](https://arxiv.org/abs/2602.03733v1) | [下载PDF](https://arxiv.org/pdf/2602.03733v1.pdf)

---

## cs.LG

## [17. Understanding and Exploiting Weight Update Sparsity for Communication-Efficient Distributed RL](https://arxiv.org/abs/2602.03839v1)

**作者**：Erfan Miahi, Eugene Belilovsky  
**分类**：cs.LG  
**发布时间**：2026-02-03

### 📄 论文摘要

Reinforcement learning (RL) is a critical component for post-training large language models (LLMs). However, in bandwidth-constrained distributed RL, scalability is often bottlenecked by the synchronization of policy weights from trainers to inference workers, particularly over commodity networks or in decentralized settings. While recent studies suggest that RL updates modify only a small fraction of model parameters, these observations are typically based on coarse checkpoint differences. We present a systematic empirical study of weight-update sparsity at both step-level and multi-step granularities, examining its evolution across training dynamics, off-policy delay, and model scale. We find that update sparsity is consistently high, frequently exceeding 99% across practically relevant settings. Leveraging this structure, we propose PULSE (Patch Updates via Lossless Sparse Encoding), a simple yet highly efficient lossless weight synchronization method that transmits only the indices and values of modified parameters. PULSE is robust to transmission errors and avoids floating-point drift inherent in additive delta schemes. In bandwidth-constrained decentralized environments, our approach achieves over 100x (14 GB to ~108 MB) communication reduction while maintaining bit-identical training dynamics and performance compared to full weight synchronization. By exploiting this structure, PULSE enables decentralized RL training to approach centralized throughput, reducing the bandwidth required for weight synchronization from 20 Gbit/s to 0.2 Gbit/s to maintain high GPU utilization.

### 🤖 AI 总结

**一句话总结**：本文提出了一种名为PULSE的高效稀疏权重同步方法，显著减少了带宽需求，同时保持训练性能。

**研究动机**：在带宽受限的分布式强化学习中，策略权重的同步常成为扩展性的瓶颈，尤其是在商品网络或去中心化环境中。

**核心方法**：PULSE方法通过传输修改参数的索引和值，利用权重更新的稀疏性，避免了浮点数漂移和传输错误。

**主要结论**：PULSE在带宽限制的去中心化环境中实现了超过100倍的通信减少，保持了与全权重同步相同的训练动态和性能。

**关键词**：权重更新稀疏性, 强化学习, 分布式RL, 大语言模型, PULSE, 通信效率, 参数同步, 训练动态, 带宽约束, llm

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2602.03839v1) | [下载PDF](https://arxiv.org/pdf/2602.03839v1.pdf)

---

## [18. Robust Intervention Learning from Emergency Stop Interventions](https://arxiv.org/abs/2602.03825v1)

**作者**：Ethan Pronovost, Khimya Khetarpal, Siddhartha Srinivasa  
**分类**：cs.LG  
**发布时间**：2026-02-03

### 📄 论文摘要

Human interventions are a common source of data in autonomous systems during testing. These interventions provide an important signal about where the current policy needs improvement, but are often noisy and incomplete. We define Robust Intervention Learning (RIL) as the problem of learning from intervention data while remaining robust to the quality and informativeness of the intervention signal. In the best case, interventions are precise and avoiding them is sufficient to solve the task, but in many realistic settings avoiding interventions is necessary but not sufficient for achieving good performance. We study robust intervention learning in the context of emergency stop interventions and propose Residual Intervention Fine-Tuning (RIFT), a residual fine-tuning algorithm that treats intervention feedback as an incomplete learning signal and explicitly combines it with a prior policy. By framing intervention learning as a fine-tuning problem, our approach leverages structure encoded in the prior policy to resolve ambiguity when intervention signals under-specify the task. We provide theoretical analysis characterizing conditions under which this formulation yields principled policy improvement, and identify regimes where intervention learning is expected to fail. Our experiments reveal that residual fine-tuning enables robust and consistent policy improvement across a range of intervention strategies and prior policy qualities, and highlight robust intervention learning as a promising direction for future work.

### 🤖 AI 总结

**一句话总结**：提出了一种稳健干预学习的方法，旨在从噪声和不完整的干预数据中学习，以改进自主系统的策略。

**研究动机**：人类干预在自主系统测试中提供了重要信号，但往往噪声大且不完整，因此需要一种方法来有效利用这些干预数据。

**核心方法**：提出了残差干预微调(RIFT)算法，将干预反馈视为不完整的学习信号，并与先验策略显式结合，以提高策略的鲁棒性。

**主要结论**：实验结果表明，残差微调能够在多种干预策略和先验策略质量下实现稳健且一致的策略改进，展示了稳健干预学习的未来应用潜力。

**关键词**：干预学习, 强健学习, 机器学习, 深度学习, 神经网络, 紧急停止干预, 残差微调, 反馈信号, 策略改进, autonomous

**评分**：68

**论文链接**：[查看原文](https://arxiv.org/abs/2602.03825v1) | [下载PDF](https://arxiv.org/pdf/2602.03825v1.pdf)

---

## [19. SymPlex: A Structure-Aware Transformer for Symbolic PDE Solving](https://arxiv.org/abs/2602.03816v1)

**作者**：Yesom Park, Annie C. Lu, Shao-Ching Huang 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-03

### 📄 论文摘要

We propose SymPlex, a reinforcement learning framework for discovering analytical symbolic solutions to partial differential equations (PDEs) without access to ground-truth expressions. SymPlex formulates symbolic PDE solving as tree-structured decision-making and optimizes candidate solutions using only the PDE and its boundary conditions. At its core is SymFormer, a structure-aware Transformer that models hierarchical symbolic dependencies via tree-relative self-attention and enforces syntactic validity through grammar-constrained autoregressive decoding, overcoming the limited expressivity of sequence-based generators. Unlike numerical and neural approaches that approximate solutions in discretized or implicit function spaces, SymPlex operates directly in symbolic expression space, enabling interpretable and human-readable solutions that naturally represent non-smooth behavior and explicit parametric dependence. Empirical results demonstrate exact recovery of non-smooth and parametric PDE solutions using deep learning-based symbolic methods.

### 🤖 AI 总结

**一句话总结**：SymPlex是一个用于符号偏微分方程求解的强化学习框架，能够在没有真实表达式的情况下发现解析符号解。

**研究动机**：现有的数值和神经方法通常在离散或隐式函数空间中近似求解，而SymPlex希望直接在符号表达空间中找到可解释的符号解。

**核心方法**：SymPlex将符号PDE求解形式化为树结构决策过程，使用结构感知的Transformer（SymFormer）通过树相对自注意力建模层次符号依赖关系，并通过语法约束的自回归解码确保语法有效性。

**主要结论**：实验证明，SymPlex能够准确恢复非光滑和参数化的PDE解，展示了深度学习基础的符号方法的有效性。

**关键词**：结构感知, Transformer, 强化学习, 符号解法, 部分微分方程, 解析解, 树结构决策, 语法约束, 自回归解码, 深度学习

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.03816v1) | [下载PDF](https://arxiv.org/pdf/2602.03816v1.pdf)

---

## [20. Enhancing Imbalanced Node Classification via Curriculum-Guided Feature Learning and Three-Stage Attention Network](https://arxiv.org/abs/2602.03808v1)

**作者**：Abdul Joseph Fofanah, Lian Wen, David Chen 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-03

### 📄 论文摘要

Imbalanced node classification in graph neural networks (GNNs) happens when some labels are much more common than others, which causes the model to learn unfairly and perform badly on the less common classes. To solve this problem, we propose a Curriculum-Guided Feature Learning and Three-Stage Attention Network (CL3AN-GNN), a learning network that uses a three-step attention system (Engage, Enact, Embed) similar to how humans learn. The model begins by engaging with structurally simpler features, defined as (1) local neighbourhood patterns (1-hop), (2) low-degree node attributes, and (3) class-separable node pairs identified via initial graph convolutional networks and graph attention networks (GCN and GAT) embeddings. This foundation enables stable early learning despite label skew. The Enact stage then addresses complicated aspects: (1) connections that require multiple steps, (2) edges that connect different types of nodes, and (3) nodes at the edges of minority classes by using adjustable attention weights. Finally, Embed consolidates these features via iterative message passing and curriculum-aligned loss weighting. We evaluate CL3AN-GNN on eight Open Graph Benchmark datasets spanning social, biological, and citation networks. Experiments show consistent improvements across all datasets in accuracy, F1-score, and AUC over recent state-of-the-art methods. The model's step-by-step method works well with different types of graph datasets, showing quicker results than training everything at once, better performance on new, imbalanced graphs, and clear explanations of each step using gradient stability and attention correlation learning curves. This work provides both a theoretically grounded framework for curriculum learning in GNNs and practical evidence of its effectiveness against imbalances, validated through metrics, convergence speeds, and generalisation tests.

### 🤖 AI 总结

**一句话总结**：提出了一种名为CL3AN-GNN的三阶段注意力网络，以解决图神经网络中的不平衡节点分类问题。

**研究动机**：不平衡的节点分类使得模型在少数类上的表现不佳，因此需要一种新的学习策略来提升模型的公平性和准确性。

**核心方法**：CL3AN-GNN通过三个阶段的注意力机制（Engage, Enact, Embed）逐步学习不同复杂度的特征，支持在标签不平衡情况下的稳定学习。

**主要结论**：实验结果表明，CL3AN-GNN在多个数据集上均优于现有方法，具备更快的收敛速度和良好的可解释性，对不平衡问题具有有效的解决方案。

**关键词**：节点分类, 图神经网络, 特征学习, 注意力机制, 课程学习, 不平衡数据, 监督学习, GNN, attention network, feature learning, neural network

**评分**：64

**论文链接**：[查看原文](https://arxiv.org/abs/2602.03808v1) | [下载PDF](https://arxiv.org/pdf/2602.03808v1.pdf)

---

## [21. Bridging Online and Offline RL: Contextual Bandit Learning for Multi-Turn Code Generation](https://arxiv.org/abs/2602.03806v1)

**作者**：Ziru Chen, Dongdong Chen, Ruinan Jin 等 6 位作者  
**分类**：cs.LG, cs.AI, cs.CL, cs.SE  
**发布时间**：2026-02-03

### 📄 论文摘要

Recently, there have been significant research interests in training large language models (LLMs) with reinforcement learning (RL) on real-world tasks, such as multi-turn code generation. While online RL tends to perform better than offline RL, its higher training cost and instability hinders wide adoption. In this paper, we build on the observation that multi-turn code generation can be formulated as a one-step recoverable Markov decision process and propose contextual bandit learning with offline trajectories (Cobalt), a new method that combines the benefits of online and offline RL. Cobalt first collects code generation trajectories using a reference LLM and divides them into partial trajectories as contextual prompts. Then, during online bandit learning, the LLM is trained to complete each partial trajectory prompt through single-step code generation. Cobalt outperforms two multi-turn online RL baselines based on GRPO and VeRPO, and substantially improves R1-Distill 8B and Qwen3 8B by up to 9.0 and 6.2 absolute Pass@1 scores on LiveCodeBench. Also, we analyze LLMs' in-context reward hacking behaviors and augment Cobalt training with perturbed trajectories to mitigate this issue. Overall, our results demonstrate Cobalt as a promising solution for iterative decision-making tasks like multi-turn code generation. Our code and data are available at https://github.com/OSU-NLP-Group/cobalt.

### 🤖 AI 总结

**一句话总结**：Cobalt是一种结合在线和离线强化学习的新方法，旨在提高多轮代码生成的性能。

**研究动机**：随着大语言模型在实际任务中的应用增多，在线强化学习的高成本和不稳定性限制了其广泛采用。

**核心方法**：Cobalt通过使用参考LLM收集代码生成轨迹，并将其分割为上下文提示，在在线赌博学习中训练LLM完成每个部分轨迹的单步代码生成。

**主要结论**：Cobalt在多轮代码生成任务中表现优越，且通过对抗性轨迹增强训练，缓解了LLM的奖励黑客行为。

**关键词**：关键词：深度学习, 机器学习, 强化学习, 多轮代码生成, 上下文赌博学习, LLM, Markov决策过程, 迭代决策任务, 代码生成轨迹

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2602.03806v1) | [下载PDF](https://arxiv.org/pdf/2602.03806v1.pdf)

---

## [22. Prediction of Critical Heat Flux in Rod Bundles Using Tube-Based Hybrid Machine Learning Models in CTF](https://arxiv.org/abs/2602.03805v1)

**作者**：Aidan Furlong, Robert Salko, Xingang Zhao 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-03

### 📄 论文摘要

The prediction of critical heat flux (CHF) using machine learning (ML) approaches has become a highly active research activity in recent years, the goal of which is to build models more accurate than current conventional approaches such as empirical correlations or lookup tables (LUTs). Previous work developed and deployed tube-based pure and hybrid ML models in the CTF subchannel code, however, full-scale reactor core simulations require the use of rod bundle geometries. Unlike isolated subchannels, rod bundles experience complex thermal hydraulic phenomena such as channel crossflow, spacer grid losses, and effects from unheated conductors. This study investigates the generalization of ML-based CHF prediction models in rod bundles after being trained on tube-based CHF data. A purely data-driven DNN and two hybrid bias-correction models were implemented in the CTF subchannel code and used to predict CHF location and magnitude in the Combustion Engineering 5-by-5 bundle CHF test series. The W-3 correlation, Bowring correlation, and Groeneveld LUT were used as baseline comparators. On average, all three ML-based approaches produced magnitude and location predictions more accurate than the baseline models, with the hybrid LUT model exhibiting the most favorable performance metrics.

### 🤖 AI 总结

**一句话总结**：本研究利用基于管道的混合机器学习模型预测棒束中的临界热流密度，表现优于传统模型。

**研究动机**：随着机器学习在临界热流密度预测中的应用日益增加，研究者希望建立比传统经验模型更准确的预测模型。

**核心方法**：研究中实现了纯数据驱动的深度神经网络和两种混合偏差校正模型，并在CTF子通道代码中进行训练和预测。

**主要结论**：所有三种基于机器学习的方法在预测热流密度的大小和位置上均优于基准模型，其中混合LUT模型表现最佳。

**关键词**：机器学习, 深度学习, 神经网络, 预测模型, 数据驱动, 复合模型, 热流密度, rod bundle, CTF, machine learning

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2602.03805v1) | [下载PDF](https://arxiv.org/pdf/2602.03805v1.pdf)

---

## [23. Manifold Random Features](https://arxiv.org/abs/2602.03797v1)

**作者**：Ananya Parashar, Derek Long, Dwaipayan Saha 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-03

### 📄 论文摘要

We present a new paradigm for creating random features to approximate bi-variate functions (in particular, kernels) defined on general manifolds. This new mechanism of Manifold Random Features (MRFs) leverages discretization of the manifold and the recently introduced technique of Graph Random Features (GRFs) to learn continuous fields on manifolds. Those fields are used to find continuous approximation mechanisms that otherwise, in general scenarios, cannot be derived analytically. MRFs provide positive and bounded features, a key property for accurate, low-variance approximation. We show deep asymptotic connection between GRFs, defined on discrete graph objects, and continuous random features used for regular kernels. As a by-product of our method, we re-discover recently introduced mechanism of Gaussian kernel approximation applied in particular to improve linear-attention Transformers, considering simple random walks on graphs and by-passing original complex mathematical computations. We complement our algorithm with a rigorous theoretical analysis and verify in thorough experimental studies.

### 🤖 AI 总结

**一句话总结**：提出了一种新的随机特征方法，用于在一般流形上近似双变量函数，特别是核函数。

**研究动机**：研究如何在复杂流形上有效地近似函数，以解决无法解析推导的连续近似机制问题。

**核心方法**：引入流形随机特征（MRFs），结合流形的离散化和图随机特征（GRFs）技术，学习流形上的连续场，从而实现准确且低方差的函数近似。

**主要结论**：通过理论分析和实验验证，MRFs能够有效改善线性注意力Transformer的性能，并简化高复杂度的数学计算。

**关键词**：随机特征, 双变量函数, 流形, 深度学习, 图随机特征, 线性注意力, 变换器, 连续近似, 低方差, 特征学习, transformer

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.03797v1) | [下载PDF](https://arxiv.org/pdf/2602.03797v1.pdf)

---

## [24. Should I use Synthetic Data for That? An Analysis of the Suitability of Synthetic Data for Data Sharing and Augmentation](https://arxiv.org/abs/2602.03791v1)

**作者**：Bogdan Kulynych, Theresa Stadler, Jean Louis Raisaro 等 4 位作者  
**分类**：cs.LG, cs.CY  
**发布时间**：2026-02-03

### 📄 论文摘要

Recent advances in generative modelling have led many to see synthetic data as the go-to solution for a range of problems around data access, scarcity, and under-representation. In this paper, we study three prominent use cases: (1) Sharing synthetic data as a proxy for proprietary datasets to enable statistical analyses while protecting privacy, (2) Augmenting machine learning training sets with synthetic data to improve model performance, and (3) Augmenting datasets with synthetic data to reduce variance in statistical estimation. For each use case, we formalise the problem setting and study, through formal analysis and case studies, under which conditions synthetic data can achieve its intended objectives. We identify fundamental and practical limits that constrain when synthetic data can serve as an effective solution for a particular problem. Our analysis reveals that due to these limits many existing or envisioned use cases of synthetic data are a poor problem fit. Our formalisations and classification of synthetic data use cases enable decision makers to assess whether synthetic data is a suitable approach for their specific data availability problem.

### 🤖 AI 总结

**一句话总结**：本论文分析了合成数据在数据共享和增强中的适用性，提出了其在特定条件下的局限性。

**研究动机**：随着生成建模的进步，合成数据被视为解决数据访问和稀缺问题的一种理想方案，本文旨在评估其实际应用潜力。

**核心方法**：通过形式化分析和案例研究，识别合成数据在三种主要使用场景下的适用条件及其局限性。

**主要结论**：研究表明，许多现有或设想的合成数据应用场景并不适合，这为决策者提供了评估合成数据适用性的框架。

**关键词**：生成数据, 生成模型, 机器学习, 数据共享, 数据增强, 统计分析, 模型性能, 变异性降低, synthetic data, 数据隐私, machine learning

**评分**：60

**论文链接**：[查看原文](https://arxiv.org/abs/2602.03791v1) | [下载PDF](https://arxiv.org/pdf/2602.03791v1.pdf)

---

## [25. Efficient Estimation of Kernel Surrogate Models for Task Attribution](https://arxiv.org/abs/2602.03783v1)

**作者**：Zhenshuo Zhang, Minxuan Duan, Hongyang R. Zhang  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-02-03

### 📄 论文摘要

Modern AI agents such as large language models are trained on diverse tasks -- translation, code generation, mathematical reasoning, and text prediction -- simultaneously. A key question is to quantify how each individual training task influences performance on a target task, a problem we refer to as task attribution. The direct approach, leave-one-out retraining, measures the effect of removing each task, but is computationally infeasible at scale. An alternative approach that builds surrogate models to predict a target task's performance for any subset of training tasks has emerged in recent literature. Prior work focuses on linear surrogate models, which capture first-order relationships, but miss nonlinear interactions such as synergy, antagonism, or XOR-type effects. In this paper, we first consider a unified task weighting framework for analyzing task attribution methods, and show a new connection between linear surrogate models and influence functions through a second-order analysis. Then, we introduce kernel surrogate models, which more effectively represent second-order task interactions. To efficiently learn the kernel surrogate, we develop a gradient-based estimation procedure that leverages a first-order approximation of pretrained models; empirically, this yields accurate estimates with less than $2\%$ relative error without repeated retraining. Experiments across multiple domains -- including math reasoning in transformers, in-context learning, and multi-objective reinforcement learning -- demonstrate the effectiveness of kernel surrogate models. They achieve a $25\%$ higher correlation with the leave-one-out ground truth than linear surrogates and influence-function baselines. When used for downstream task selection, kernel surrogate models yield a $40\%$ improvement in demonstration selection for in-context learning and multi-objective reinforcement learning benchmarks.

### 🤖 AI 总结

**一句话总结**：本文提出了一种高效的核代理模型，用于分析任务归属，克服了线性代理模型在捕捉非线性交互方面的局限。

**研究动机**：现代AI代理同时在多种任务上进行训练，理解每个训练任务对目标任务性能的影响是至关重要的，但传统的方法在大规模上计算不可行。

**核心方法**：文章提出了基于梯度的核代理模型估计程序，能够有效地表示任务间的二阶交互，同时通过一阶近似加速学习过程。

**主要结论**：实验结果表明，核代理模型在多种领域中的性能评估上比线性代理更为准确，且在下游任务选择中显著提高了表现。

**关键词**：任务归因, 核心代理模型, 机器学习, 深度学习, 代理, 预训练模型, 任务加权框架, 多目标强化学习, 上下文学习, 性能预测, agent

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.03783v1) | [下载PDF](https://arxiv.org/pdf/2602.03783v1.pdf)

---

## [26. Reward Redistribution for CVaR MDPs using a Bellman Operator on L-infinity](https://arxiv.org/abs/2602.03778v1)

**作者**：Aneri Muni, Vincent Taboga, Esther Derman 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-03

### 📄 论文摘要

Tail-end risk measures such as static conditional value-at-risk (CVaR) are used in safety-critical applications to prevent rare, yet catastrophic events. Unlike risk-neutral objectives, the static CVaR of the return depends on entire trajectories without admitting a recursive Bellman decomposition in the underlying Markov decision process. A classical resolution relies on state augmentation with a continuous variable. However, unless restricted to a specialized class of admissible value functions, this formulation induces sparse rewards and degenerate fixed points. In this work, we propose a novel formulation of the static CVaR objective based on augmentation. Our alternative approach leads to a Bellman operator with: (1) dense per-step rewards; (2) contracting properties on the full space of bounded value functions. Building on this theoretical foundation, we develop risk-averse value iteration and model-free Q-learning algorithms that rely on discretized augmented states. We further provide convergence guarantees and approximation error bounds due to discretization. Empirical results demonstrate that our algorithms successfully learn CVaR-sensitive policies and achieve effective performance-safety trade-offs.

### 🤖 AI 总结

**一句话总结**：本研究提出了一种基于增强的静态条件价值-at-risk (CVaR)目标的新公式，通过贝尔曼算子实现风险厌恶的价值迭代和无模型Q学习算法。

**研究动机**：在安全关键应用中，传统的风险中性目标无法有效处理尾部风险，因此需要新的方法来更好地管理稀有但灾难性的事件。

**核心方法**：通过状态增强的方法提出静态CVaR目标的新公式，从而获得稠密的每步奖励和收敛性质，并开发相应的算法。

**主要结论**：实验结果表明，所提出的算法能够成功学习对CVaR敏感的策略，并实现有效的性能与安全权衡。

**关键词**：奖励再分配, CVaR, 马尔可夫决策过程, 风险规避, 值迭代, 强化学习, Bellman算子, 稠密奖励, 近似误差界限

**评分**：54

**论文链接**：[查看原文](https://arxiv.org/abs/2602.03778v1) | [下载PDF](https://arxiv.org/pdf/2602.03778v1.pdf)

---

## [27. Decision-oriented benchmarking to transform AI weather forecast access: Application to the Indian monsoon](https://arxiv.org/abs/2602.03767v1)

**作者**：Rajat Masiwal, Colin Aitken, Adam Marchakitus 等 12 位作者  
**分类**：cs.LG, cs.AI, econ.GN, physics.ao-ph  
**发布时间**：2026-02-03

### 📄 论文摘要

Artificial intelligence weather prediction (AIWP) models now often outperform traditional physics-based models on common metrics while requiring orders-of-magnitude less computing resources and time. Open-access AIWP models thus hold promise as transformational tools for helping low- and middle-income populations make decisions in the face of high-impact weather shocks. Yet, current approaches to evaluating AIWP models focus mainly on aggregated meteorological metrics without considering local stakeholders' needs in decision-oriented, operational frameworks. Here, we introduce such a framework that connects meteorology, AI, and social sciences. As an example, we apply it to the 150-year-old problem of Indian monsoon forecasting, focusing on benefits to rain-fed agriculture, which is highly susceptible to climate change. AIWP models skillfully predict an agriculturally relevant onset index at regional scales weeks in advance when evaluated out-of-sample using deterministic and probabilistic metrics. This framework informed a government-led effort in 2025 to send 38 million Indian farmers AI-based monsoon onset forecasts, which captured an unusual weeks-long pause in monsoon progression. This decision-oriented benchmarking framework provides a key component of a blueprint for harnessing the power of AIWP models to help large vulnerable populations adapt to weather shocks in the face of climate variability and change.

### 🤖 AI 总结

**一句话总结**：该研究提出了一种决策导向的基准评估框架，以提升AI天气预报在印度季风预测中的应用，帮助农民应对气候变化带来的影响。

**研究动机**：当前的AI天气预报模型在性能上优于传统模型，但评估方法未能满足当地利益相关者的决策需求，因此需要一种新的评估框架。

**核心方法**：研究引入了一个结合气象学、人工智能和社会科学的决策导向框架，并应用于印度季风的预测，特别关注对雨养农业的影响。

**主要结论**：该框架为利用AI天气预报模型帮助脆弱人群适应气候变化提供了重要的参考，成功地为3800万农民提供了季风预测信息。

**关键词**：气象预测, 机器学习, 深度学习, 神经网络, 决策导向, 农业适应, AI天气预测, 预测模型, 气候变化, 农民助手

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.03767v1) | [下载PDF](https://arxiv.org/pdf/2602.03767v1.pdf)

---

## [28. Soft Sensor for Bottom-Hole Pressure Estimation in Petroleum Wells Using Long Short-Term Memory and Transfer Learning](https://arxiv.org/abs/2602.03737v1)

**作者**：M. A. Fernandes, E. Gildin, M. A. Sampaio  
**分类**：cs.LG  
**发布时间**：2026-02-03

### 📄 论文摘要

Monitoring bottom-hole variables in petroleum wells is essential for production optimization, safety, and emissions reduction. Permanent Downhole Gauges (PDGs) provide real-time pressure data but face reliability and cost issues. We propose a machine learning-based soft sensor to estimate flowing Bottom-Hole Pressure (BHP) using wellhead and topside measurements. A Long Short-Term Memory (LSTM) model is introduced and compared with Multi-Layer Perceptron (MLP) and Ridge Regression. We also pioneer Transfer Learning for adapting models across operational environments. Tested on real offshore datasets from Brazil's Pre-salt basin, the methodology achieved Mean Absolute Percentage Error (MAPE) consistently below 2\%, outperforming benchmarks. This work offers a cost-effective, accurate alternative to physical sensors, with broad applicability across diverse reservoir and flow conditions.

### 🤖 AI 总结

**一句话总结**：本研究提出了一种基于LSTM和迁移学习的软传感器，用于准确估计石油井的底部压力，且在实际数据测试中表现优异。

**研究动机**：监测石油井底部变量对于优化生产、安全和减少排放至关重要，但现有的永久井下传感器存在可靠性和成本问题。

**核心方法**：引入长短期记忆（LSTM）模型，并与多层感知器（MLP）和岭回归进行比较，同时应用迁移学习以适应不同的操作环境。

**主要结论**：该方法在巴西预盐盆地的实际数据集上测试，平均绝对百分比误差（MAPE）始终低于2%，为物理传感器提供了一种成本效益高且准确的替代方案。

**关键词**：底部压力, 软传感器, 机器学习, LSTM, 转移学习, 多层感知器, 准确性, 实时监测, 数据适应, machine learning

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2602.03737v1) | [下载PDF](https://arxiv.org/pdf/2602.03737v1.pdf)

---

## [29. Fast-MWEM: Private Data Release in Sublinear Time](https://arxiv.org/abs/2602.03732v1)

**作者**：Themistoklis Haris, Steve Choi, Mutiraj Laksanawisit  
**分类**：cs.LG  
**发布时间**：2026-02-03

### 📄 论文摘要

The Multiplicative Weights Exponential Mechanism (MWEM) is a fundamental iterative framework for private data analysis, with broad applications such as answering $m$ linear queries, or privately solving systems of $m$ linear constraints. However, a critical bottleneck hindering its scalability is the $Θ(m)$ time complexity required to execute the exponential mechanism in each iteration. We introduce a modification to the MWEM framework that improves the per-iteration runtime dependency to $Θ(\sqrt{m})$ in expectation. This is done via a lazy sampling approach to the Report-Noisy-Max mechanism, which we implement efficiently using Gumbel noise and a $k$-Nearest Neighbor data structure. This allows for the rapid selection of the approximate score in the exponential mechanism without an exhaustive linear scan. We apply our accelerated framework to the problems of private linear query release and solving Linear Programs (LPs) under neighboring constraint conditions and low-sensitivity assumptions. Experimental evaluation confirms that our method provides a substantial runtime improvement over classic MWEM.

### 🤖 AI 总结

**一句话总结**：Fast-MWEM通过懒采样方法将MWEM框架的每次迭代时间复杂度降低至Θ(√m)，显著提高了私有数据发布的效率。

**研究动机**：MWEM框架在执行每次迭代时需要Θ(m)的时间复杂度，影响了其可扩展性，因此需要寻找更高效的实现方式。

**核心方法**：采用懒采样的Report-Noisy-Max机制，结合Gumbel噪声和k-近邻数据结构，优化每次迭代的运行时间至Θ(√m)。

**主要结论**：实验结果表明，Fast-MWEM在私有线性查询发布和解决线性规划问题上，相较于经典MWEM方法显著提升了运行效率。

**关键词**：私有数据发布, 多重权重指数机制, 线性查询, 线性约束, Gumbel噪声, k-近邻数据结构, 近似评分, 数据分析, 迭代框架, agent

**评分**：68

**论文链接**：[查看原文](https://arxiv.org/abs/2602.03732v1) | [下载PDF](https://arxiv.org/pdf/2602.03732v1.pdf)

---

## [30. Efficient Training of Boltzmann Generators Using Off-Policy Log-Dispersion Regularization](https://arxiv.org/abs/2602.03729v1)

**作者**：Henrik Schopmans, Christopher von Klitzing, Pascal Friederich  
**分类**：cs.LG  
**发布时间**：2026-02-03

### 📄 论文摘要

Sampling from unnormalized probability densities is a central challenge in computational science. Boltzmann generators are generative models that enable independent sampling from the Boltzmann distribution of physical systems at a given temperature. However, their practical success depends on data-efficient training, as both simulation data and target energy evaluations are costly. To this end, we propose off-policy log-dispersion regularization (LDR), a novel regularization framework that builds on a generalization of the log-variance objective. We apply LDR in the off-policy setting in combination with standard data-based training objectives, without requiring additional on-policy samples. LDR acts as a shape regularizer of the energy landscape by leveraging additional information in the form of target energy labels. The proposed regularization framework is broadly applicable, supporting unbiased or biased simulation datasets as well as purely variational training without access to target samples. Across all benchmarks, LDR improves both final performance and data efficiency, with sample efficiency gains of up to one order of magnitude.

### 🤖 AI 总结

**一句话总结**：提出了一种新颖的离线政策对数散布正则化方法，以提高Boltzmann生成器的训练效率和数据利用率。

**研究动机**：在计算科学中，从未归一化概率密度中采样是一项重要挑战，而Boltzmann生成器在此过程中依赖于高效的数据训练。

**核心方法**：提出的离线政策对数散布正则化（LDR）在不需要额外样本的情况下，结合标准数据训练目标，以改善能量景观的形状。

**主要结论**：LDR在所有基准测试中都提高了最终性能和数据效率，样本效率提升可达一个数量级。

**关键词**：生成模型, 采样, 训练, 正则化, Boltzmann生成器, 数据效率, 能量标签, 离线学习, 生成模型优化, 物理系统, generative

**评分**：69

**论文链接**：[查看原文](https://arxiv.org/abs/2602.03729v1) | [下载PDF](https://arxiv.org/pdf/2602.03729v1.pdf)

---

