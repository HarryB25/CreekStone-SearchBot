# arXiv AI 论文日报 | 2026-02-10

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (8 篇)
- [cs.LG](#csLG) (13 篇)
- [cs.AI](#csAI) (6 篇)
- [cs.CL](#csCL) (3 篇)

---

## cs.AI

## [1. GEBench: Benchmarking Image Generation Models as GUI Environments](https://arxiv.org/abs/2602.09007v1)

**作者**：Haodong Li, Jingwei Wu, Quan Sun 等 17 位作者  
**分类**：cs.AI, cs.CV  
**发布时间**：2026-02-09

### 📄 论文摘要

Recent advancements in image generation models have enabled the prediction of future Graphical User Interface (GUI) states based on user instructions. However, existing benchmarks primarily focus on general domain visual fidelity, leaving the evaluation of state transitions and temporal coherence in GUI-specific contexts underexplored. To address this gap, we introduce GEBench, a comprehensive benchmark for evaluating dynamic interaction and temporal coherence in GUI generation. GEBench comprises 700 carefully curated samples spanning five task categories, covering both single-step interactions and multi-step trajectories across real-world and fictional scenarios, as well as grounding point localization. To support systematic evaluation, we propose GE-Score, a novel five-dimensional metric that assesses Goal Achievement, Interaction Logic, Content Consistency, UI Plausibility, and Visual Quality. Extensive evaluations on current models indicate that while they perform well on single-step transitions, they struggle significantly with maintaining temporal coherence and spatial grounding over longer interaction sequences. Our findings identify icon interpretation, text rendering, and localization precision as critical bottlenecks. This work provides a foundation for systematic assessment and suggests promising directions for future research toward building high-fidelity generative GUI environments. The code is available at: https://github.com/stepfun-ai/GEBench.

### 🤖 AI 总结

**一句话总结**：Recent advancements in image generation models have enabled the prediction of future Graphical User Interface (GUI) states based on user instructions. However, existing benchmarks primarily focus on g...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：existing benchmarks primarily focus on general domain visual fidelity, specific contexts underexplored. To address this gap, they struggle significantly with maintaining temporal coherence and spatial grounding over longer interaction sequences. Our findings identify icon interpretation, fidelity generative GUI environments. The code is available at: https://github.com/stepfun, ai/GEBench.

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.09007v1) | [下载PDF](https://arxiv.org/pdf/2602.09007v1.pdf)

---

## [2. Data Science and Technology Towards AGI Part I: Tiered Data Management](https://arxiv.org/abs/2602.09003v1)

**作者**：Yudong Wang, Zixuan Fu, Hengyu Zhao 等 17 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-02-09

### 📄 论文摘要

The development of artificial intelligence can be viewed as an evolution of data-driven learning paradigms, with successive shifts in data organization and utilization continuously driving advances in model capability. Current LLM research is dominated by a paradigm that relies heavily on unidirectional scaling of data size, increasingly encountering bottlenecks in data availability, acquisition cost, and training efficiency. In this work, we argue that the development of AGI is entering a new phase of data-model co-evolution, in which models actively guide data management while high-quality data, in turn, amplifies model capabilities. To implement this vision, we propose a tiered data management framework, designed to support the full LLM training lifecycle across heterogeneous learning objectives and cost constraints. Specifically, we introduce an L0-L4 tiered data management framework, ranging from raw uncurated resources to organized and verifiable knowledge. Importantly, LLMs are fully used in data management processes, such as quality scoring and content editing, to refine data across tiers. Each tier is characterized by distinct data properties, management strategies, and training roles, enabling data to be strategically allocated across LLM training stages, including pre-training, mid-training, and alignment. The framework balances data quality, acquisition cost, and marginal training benefit, providing a systematic approach to scalable and sustainable data management. We validate the effectiveness of the proposed framework through empirical studies, in which tiered datasets are constructed from raw corpora and used across multiple training phases. Experimental results demonstrate that tier-aware data utilization significantly improves training efficiency and model performance. To facilitate further research, we release our tiered datasets and processing tools to the community.

### 🤖 AI 总结

**一句话总结**：The development of artificial intelligence can be viewed as an evolution of data-driven learning paradigms, with successive shifts in data organization and utilization continuously driving advances in...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：The development of artificial intelligence can be viewed as an evolution of data, with successive shifts in data organization and utilization continuously driving advances in model capability. Current LLM research is dominated by a paradigm that relies heavily on unidirectional scaling of data size, increasingly encountering bottlenecks in data availability, and training efficiency. In this work, designed to support the full LLM training lifecycle across heterogeneous learning objectives and cost constraints. Specifically, LLMs are fully used in data management processes, and training roles, enabling data to be strategically allocated across LLM training stages, training, and marginal training benefit, providing a systematic approach to scalable and sustainable data management. We validate the effectiveness of the proposed framework through empirical studies, in which tiered datasets are constructed from raw corpora and used across multiple training phases. Experimental results demonstrate that tier, aware data utilization significantly improves training efficiency and model performance. To facilitate further research

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.09003v1) | [下载PDF](https://arxiv.org/pdf/2602.09003v1.pdf)

---

## [3. InternAgent-1.5: A Unified Agentic Framework for Long-Horizon Autonomous Scientific Discovery](https://arxiv.org/abs/2602.08990v1)

**作者**：Shiyang Feng, Runmin Ma, Xiangchao Yan 等 57 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-09

### 📄 论文摘要

We introduce InternAgent-1.5, a unified system designed for end-to-end scientific discovery across computational and empirical domains. The system is built on a structured architecture composed of three coordinated subsystems for generation, verification, and evolution. These subsystems are supported by foundational capabilities for deep research, solution optimization, and long horizon memory. The architecture allows InternAgent-1.5 to operate continuously across extended discovery cycles while maintaining coherent and improving behavior. It also enables the system to coordinate computational modeling and laboratory experimentation within a single unified system. We evaluate InternAgent-1.5 on scientific reasoning benchmarks such as GAIA, HLE, GPQA, and FrontierScience, and the system achieves leading performance that demonstrates strong foundational capabilities. Beyond these benchmarks, we further assess two categories of discovery tasks. In algorithm discovery tasks, InternAgent-1.5 autonomously designs competitive methods for core machine learning problems. In empirical discovery tasks, it executes complete computational or wet lab experiments and produces scientific findings in earth, life, biological, and physical domains. Overall, these results show that InternAgent-1.5 provides a general and scalable framework for autonomous scientific discovery.

### 🤖 AI 总结

**一句话总结**：We introduce InternAgent-1.5, a unified system designed for end-to-end scientific discovery across computational and empirical domains. The system is built on a structured architecture composed of thr...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：InternAgent, 1.5: A Unified Agentic Framework for Long, Horizon Autonomous Scientific Discovery, We introduce InternAgent, end scientific discovery across computational and empirical domains. The system is built on a structured architecture composed of three coordinated subsystems for generation, and long horizon memory. The architecture allows InternAgent, 1.5 to operate continuously across extended discovery cycles while maintaining coherent and improving behavior. It also enables the system to coordinate computational modeling and laboratory experimentation within a single unified system. We evaluate InternAgent, 1.5 on scientific reasoning benchmarks such as GAIA, 1.5 autonomously designs competitive methods for core machine learning problems. In empirical discovery tasks, and physical domains. Overall, these results show that InternAgent, 1.5 provides a general and scalable framework for autonomous scientific discovery.

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.08990v1) | [下载PDF](https://arxiv.org/pdf/2602.08990v1.pdf)

---

## [4. stable-worldmodel-v1: Reproducible World Modeling Research and Evaluation](https://arxiv.org/abs/2602.08968v1)

**作者**：Lucas Maes, Quentin Le Lidec, Dan Haramati 等 7 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-09

### 📄 论文摘要

World Models have emerged as a powerful paradigm for learning compact, predictive representations of environment dynamics, enabling agents to reason, plan, and generalize beyond direct experience. Despite recent interest in World Models, most available implementations remain publication-specific, severely limiting their reusability, increasing the risk of bugs, and reducing evaluation standardization. To mitigate these issues, we introduce stable-worldmodel (SWM), a modular, tested, and documented world-model research ecosystem that provides efficient data-collection tools, standardized environments, planning algorithms, and baseline implementations. In addition, each environment in SWM enables controllable factors of variation, including visual and physical properties, to support robustness and continual learning research. Finally, we demonstrate the utility of SWM by using it to study zero-shot robustness in DINO-WM.

### 🤖 AI 总结

**一句话总结**：World Models have emerged as a powerful paradigm for learning compact, predictive representations of environment dynamics, enabling agents to reason, plan, and generalize beyond direct experience. Des...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：enabling agents to reason, most available implementations remain publication

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.08968v1) | [下载PDF](https://arxiv.org/pdf/2602.08968v1.pdf)

---

## [5. Digital Twin and Agentic AI for Wild Fire Disaster Management: Intelligent Virtual Situation Room](https://arxiv.org/abs/2602.08949v1)

**作者**：Mohammad Morsali, Siavash H. Khajavi  
**分类**：cs.AI, cs.SE  
**发布时间**：2026-02-09

### 📄 论文摘要

According to the United Nations, wildfire frequency and intensity are projected to increase by approximately 14% by 2030 and 30% by 2050 due to global warming, posing critical threats to life, infrastructure, and ecosystems. Conventional disaster management frameworks rely on static simulations and passive data acquisition, hindering their ability to adapt to arbitrarily evolving wildfire episodes in real-time. To address these limitations, we introduce the Intelligent Virtual Situation Room (IVSR), a bidirectional Digital Twin (DT) platform augmented by autonomous AI agents. The IVSR continuously ingests multisource sensor imagery, weather data, and 3D forest models to create a live virtual replica of the fire environment. A similarity engine powered by AI aligns emerging conditions with a precomputed Disaster Simulation Library, retrieving and calibrating intervention tactics under the watchful eyes of experts. Authorized action-ranging from UAV redeployment to crew reallocation-is cycled back through standardized procedures to the physical layer, completing the loop between response and analysis. We validate IVSR through detailed case-study simulations provided by an industrial partner, demonstrating capabilities in localized incident detection, privacy-preserving playback, collider-based fire-spread projection, and site-specific ML retraining. Our results indicate marked reductions in detection-to-intervention latency and more effective resource coordination versus traditional systems. By uniting real-time bidirectional DTs with agentic AI, IVSR offers a scalable, semi-automated decision-support paradigm for proactive, adaptive wildfire disaster management.

### 🤖 AI 总结

**一句话总结**：According to the United Nations, wildfire frequency and intensity are projected to increase by approximately 14% by 2030 and 30% by 2050 due to global warming, posing critical threats to life, infrast...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：Digital Twin and Agentic AI for Wild Fire Disaster Management: Intelligent Virtual Situation Room, a bidirectional Digital Twin (DT) platform augmented by autonomous AI agents. The IVSR continuously ingests multisource sensor imagery, and 3D forest models to create a live virtual replica of the fire environment. A similarity engine powered by AI aligns emerging conditions with a precomputed Disaster Simulation Library, completing the loop between response and analysis. We validate IVSR through detailed case, specific ML retraining. Our results indicate marked reductions in detection, time bidirectional DTs with agentic AI

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.08949v1) | [下载PDF](https://arxiv.org/pdf/2602.08949v1.pdf)

---

## [6. CausalT5K: Diagnosing and Informing Refusal for Trustworthy Causal Reasoning of Skepticism, Sycophancy, Detection-Correction, and Rung Collapse](https://arxiv.org/abs/2602.08939v1)

**作者**：Longling Geng, Andy Ouyang, Theodore Wu 等 13 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-09

### 📄 论文摘要

LLM failures in causal reasoning, including sycophancy, rung collapse, and miscalibrated refusal, are well-documented, yet progress on remediation is slow because no benchmark enables systematic diagnosis. We introduce CausalT5K, a diagnostic benchmark of over 5,000 cases across 10 domains that tests three critical capabilities: (1) detecting rung collapse, where models answer interventional queries with associational evidence; (2) resisting sycophantic drift under adversarial pressure; and (3) generating Wise Refusals that specify missing information when evidence is underdetermined. Unlike synthetic benchmarks, CausalT5K embeds causal traps in realistic narratives and decomposes performance into Utility (sensitivity) and Safety (specificity), revealing failure modes invisible to aggregate accuracy. Developed through a rigorous human-machine collaborative pipeline involving 40 domain experts, iterative cross-validation cycles, and composite verification via rule-based, LLM, and human scoring, CausalT5K implements Pearl's Ladder of Causation as research infrastructure. Preliminary experiments reveal a Four-Quadrant Control Landscape where static audit policies universally fail, a finding that demonstrates CausalT5K's value for advancing trustworthy reasoning systems. Repository: https://github.com/genglongling/CausalT5kBench

### 🤖 AI 总结

**一句话总结**：LLM failures in causal reasoning, including sycophancy, rung collapse, and miscalibrated refusal, are well-documented, yet progress on remediation is slow because no benchmark enables systematic diagn...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：LLM failures in causal reasoning, 000 cases across 10 domains that tests three critical capabilities: (1) detecting rung collapse, revealing failure modes invisible to aggregate accuracy. Developed through a rigorous human, machine collaborative pipeline involving 40 domain experts, LLM, Quadrant Control Landscape where static audit policies universally fail

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.08939v1) | [下载PDF](https://arxiv.org/pdf/2602.08939v1.pdf)

---

## cs.CL

## [7. When Actions Go Off-Task: Detecting and Correcting Misaligned Actions in Computer-Use Agents](https://arxiv.org/abs/2602.08995v1)

**作者**：Yuting Ning, Jaylen Jones, Zhehao Zhang 等 8 位作者  
**分类**：cs.CL  
**发布时间**：2026-02-09

### 📄 论文摘要

Computer-use agents (CUAs) have made tremendous progress in the past year, yet they still frequently produce misaligned actions that deviate from the user's original intent. Such misaligned actions may arise from external attacks (e.g., indirect prompt injection) or from internal limitations (e.g., erroneous reasoning). They not only expose CUAs to safety risks, but also degrade task efficiency and reliability. This work makes the first effort to define and study misaligned action detection in CUAs, with comprehensive coverage of both externally induced and internally arising misaligned actions. We further identify three common categories in real-world CUA deployment and construct MisActBench, a benchmark of realistic trajectories with human-annotated, action-level alignment labels. Moreover, we propose DeAction, a practical and universal guardrail that detects misaligned actions before execution and iteratively corrects them through structured feedback. DeAction outperforms all existing baselines across offline and online evaluations with moderate latency overhead: (1) On MisActBench, it outperforms baselines by over 15% absolute in F1 score; (2) In online evaluation, it reduces attack success rate by over 90% under adversarial settings while preserving or even improving task success rate in benign environments.

### 🤖 AI 总结

**一句话总结**：Computer-use agents (CUAs) have made tremendous progress in the past year, yet they still frequently produce misaligned actions that deviate from the user's original intent. Such misaligned actions ma...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：Use Agents, use agents (CUAs) have made tremendous progress in the past year, with comprehensive coverage of both externally induced and internally arising misaligned actions. We further identify three common categories in real, a practical and universal guardrail that detects misaligned actions before execution and iteratively corrects them through structured feedback. DeAction outperforms all existing baselines across offline and online evaluations with moderate latency overhead: (1) On MisActBench

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.08995v1) | [下载PDF](https://arxiv.org/pdf/2602.08995v1.pdf)

---

## [8. How Should We Model the Probability of a Language?](https://arxiv.org/abs/2602.08951v1)

**作者**：Rasul Dent, Pedro Ortiz Suarez, Thibault Clérice 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-02-09

### 📄 论文摘要

Of the over 7,000 languages spoken in the world, commercial language identification (LID) systems only reliably identify a few hundred in written form. Research-grade systems extend this coverage under certain circumstances, but for most languages coverage remains patchy or nonexistent. This position paper argues that this situation is largely self-imposed. In particular, it arises from a persistent framing of LID as decontextualized text classification, which obscures the central role of prior probability estimation and is reinforced by institutional incentives that favor global, fixed-prior models. We argue that improving coverage for tail languages requires rethinking LID as a routing problem and developing principled ways to incorporate environmental cues that make languages locally plausible.

### 🤖 AI 总结

**一句话总结**：Of the over 7,000 languages spoken in the world, commercial language identification (LID) systems only reliably identify a few hundred in written form. Research-grade systems extend this coverage unde...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：grade systems extend this coverage under certain circumstances, but for most languages coverage remains patchy or nonexistent. This position paper argues that this situation is largely self, it arises from a persistent framing of LID as decontextualized text classification, prior models. We argue that improving coverage for tail languages requires rethinking LID as a routing problem and developing principled ways to incorporate environmental cues that make languages locally plausible.

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.08951v1) | [下载PDF](https://arxiv.org/pdf/2602.08951v1.pdf)

---

## [9. GitSearch: Enhancing Community Notes Generation with Gap-Informed Targeted Search](https://arxiv.org/abs/2602.08945v1)

**作者**：Sahajpreet Singh, Kokil Jaidka, Min-Yen Kan  
**分类**：cs.CL, cs.CY  
**发布时间**：2026-02-09

### 📄 论文摘要

Community-based moderation offers a scalable alternative to centralized fact-checking, yet it faces significant structural challenges, and existing AI-based methods fail in "cold start" scenarios. To tackle these challenges, we introduce GitSearch (Gap-Informed Targeted Search), a framework that treats human-perceived quality gaps, such as missing context, etc., as first-class signals. GitSearch has a three-stage pipeline: identifying information deficits, executing real-time targeted web-retrieval to resolve them, and synthesizing platform-compliant notes. To facilitate evaluation, we present PolBench, a benchmark of 78,698 U.S. political tweets with their associated Community Notes. We find GitSearch achieves 99% coverage, almost doubling coverage over the state-of-the-art. GitSearch surpasses human-authored helpful notes with a 69% win rate and superior helpfulness scores (3.87 vs. 3.36), demonstrating retrieval effectiveness that balanced the trade-off between scale and quality.

### 🤖 AI 总结

**一句话总结**：Community-based moderation offers a scalable alternative to centralized fact-checking, yet it faces significant structural challenges, and existing AI-based methods fail in "cold start" scenarios. To ...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：and existing AI, based methods fail in "cold start" scenarios. To tackle these challenges, such as missing context, retrieval to resolve them, 698 U.S. political tweets with their associated Community Notes. We find GitSearch achieves 99% coverage, almost doubling coverage over the state, demonstrating retrieval effectiveness that balanced the trade

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.08945v1) | [下载PDF](https://arxiv.org/pdf/2602.08945v1.pdf)

---

## cs.CV

## [10. WorldCompass: Reinforcement Learning for Long-Horizon World Models](https://arxiv.org/abs/2602.09022v1)

**作者**：Zehan Wang, Tengfei Wang, Haiyu Zhang 等 12 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-09

### 📄 论文摘要

This work presents WorldCompass, a novel Reinforcement Learning (RL) post-training framework for the long-horizon, interactive video-based world models, enabling them to explore the world more accurately and consistently based on interaction signals. To effectively "steer" the world model's exploration, we introduce three core innovations tailored to the autoregressive video generation paradigm: 1) Clip-level rollout Strategy: We generate and evaluate multiple samples at a single target clip, which significantly boosts rollout efficiency and provides fine-grained reward signals. 2) Complementary Reward Functions: We design reward functions for both interaction-following accuracy and visual quality, which provide direct supervision and effectively suppress reward-hacking behaviors. 3) Efficient RL Algorithm: We employ the negative-aware fine-tuning strategy coupled with various efficiency optimizations to efficiently and effectively enhance model capacity. Evaluations on the SoTA open-source world model, WorldPlay, demonstrate that WorldCompass significantly improves interaction accuracy and visual fidelity across various scenarios.

### 🤖 AI 总结

**一句话总结**：This work presents WorldCompass, a novel Reinforcement Learning (RL) post-training framework for the long-horizon, interactive video-based world models, enabling them to explore the world more accurat...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：training framework for the long, we introduce three core innovations tailored to the autoregressive video generation paradigm: 1) Clip, grained reward signals. 2) Complementary Reward Functions: We design reward functions for both interaction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.09022v1) | [下载PDF](https://arxiv.org/pdf/2602.09022v1.pdf)

---

## [11. Raster2Seq: Polygon Sequence Generation for Floorplan Reconstruction](https://arxiv.org/abs/2602.09016v1)

**作者**：Hao Phung, Hadar Averbuch-Elor  
**分类**：cs.CV  
**发布时间**：2026-02-09

### 📄 论文摘要

Reconstructing a structured vector-graphics representation from a rasterized floorplan image is typically an important prerequisite for computational tasks involving floorplans such as automated understanding or CAD workflows. However, existing techniques struggle in faithfully generating the structure and semantics conveyed by complex floorplans that depict large indoor spaces with many rooms and a varying numbers of polygon corners. To this end, we propose Raster2Seq, framing floorplan reconstruction as a sequence-to-sequence task in which floorplan elements--such as rooms, windows, and doors--are represented as labeled polygon sequences that jointly encode geometry and semantics. Our approach introduces an autoregressive decoder that learns to predict the next corner conditioned on image features and previously generated corners using guidance from learnable anchors. These anchors represent spatial coordinates in image space, hence allowing for effectively directing the attention mechanism to focus on informative image regions. By embracing the autoregressive mechanism, our method offers flexibility in the output format, enabling for efficiently handling complex floorplans with numerous rooms and diverse polygon structures. Our method achieves state-of-the-art performance on standard benchmarks such as Structure3D, CubiCasa5K, and Raster2Graph, while also demonstrating strong generalization to more challenging datasets like WAFFLE, which contain diverse room structures and complex geometric variations.

### 🤖 AI 总结

**一句话总结**：Reconstructing a structured vector-graphics representation from a rasterized floorplan image is typically an important prerequisite for computational tasks involving floorplans such as automated under...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：Reconstructing a structured vector, graphics representation from a rasterized floorplan image is typically an important prerequisite for computational tasks involving floorplans such as automated understanding or CAD workflows. However, existing techniques struggle in faithfully generating the structure and semantics conveyed by complex floorplans that depict large indoor spaces with many rooms and a varying numbers of polygon corners. To this end, which contain diverse room structures and complex geometric variations.

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.09016v1) | [下载PDF](https://arxiv.org/pdf/2602.09016v1.pdf)

---

## [12. ArcFlow: Unleashing 2-Step Text-to-Image Generation via High-Precision Non-Linear Flow Distillation](https://arxiv.org/abs/2602.09014v1)

**作者**：Zihan Yang, Shuyuan Tu, Licheng Zhang 等 6 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-02-09

### 📄 论文摘要

Diffusion models have achieved remarkable generation quality, but they suffer from significant inference cost due to their reliance on multiple sequential denoising steps, motivating recent efforts to distill this inference process into a few-step regime. However, existing distillation methods typically approximate the teacher trajectory by using linear shortcuts, which makes it difficult to match its constantly changing tangent directions as velocities evolve across timesteps, thereby leading to quality degradation. To address this limitation, we propose ArcFlow, a few-step distillation framework that explicitly employs non-linear flow trajectories to approximate pre-trained teacher trajectories. Concretely, ArcFlow parameterizes the velocity field underlying the inference trajectory as a mixture of continuous momentum processes. This enables ArcFlow to capture velocity evolution and extrapolate coherent velocities to form a continuous non-linear trajectory within each denoising step. Importantly, this parameterization admits an analytical integration of this non-linear trajectory, which circumvents numerical discretization errors and results in high-precision approximation of the teacher trajectory. To train this parameterization into a few-step generator, we implement ArcFlow via trajectory distillation on pre-trained teacher models using lightweight adapters. This strategy ensures fast, stable convergence while preserving generative diversity and quality. Built on large-scale models (Qwen-Image-20B and FLUX.1-dev), ArcFlow only fine-tunes on less than 5% of original parameters and achieves a 40x speedup with 2 NFEs over the original multi-step teachers without significant quality degradation. Experiments on benchmarks show the effectiveness of ArcFlow both qualitatively and quantitatively.

### 🤖 AI 总结

**一句话总结**：Diffusion models have achieved remarkable generation quality, but they suffer from significant inference cost due to their reliance on multiple sequential denoising steps, motivating recent efforts to...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：Diffusion models have achieved remarkable generation quality, trained teacher trajectories. Concretely, precision approximation of the teacher trajectory. To train this parameterization into a few, trained teacher models using lightweight adapters. This strategy ensures fast, stable convergence while preserving generative diversity and quality. Built on large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.09014v1) | [下载PDF](https://arxiv.org/pdf/2602.09014v1.pdf)

---

## [13. Generalizing Sports Feedback Generation by Watching Competitions and Reading Books: A Rock Climbing Case Study](https://arxiv.org/abs/2602.08996v1)

**作者**：Arushi Rai, Adriana Kovashka  
**分类**：cs.CV  
**发布时间**：2026-02-09

### 📄 论文摘要

While there is rapid progress in video-LLMs with advanced reasoning capabilities, prior work shows that these models struggle on the challenging task of sports feedback generation and require expensive and difficult-to-collect finetuning feedback data for each sport. This limitation is evident from the poor generalization to sports unseen during finetuning. Furthermore, traditional text generation evaluation metrics (e.g., BLEU-4, METEOR, ROUGE-L, BERTScore), originally developed for machine translation and summarization, fail to capture the unique aspects of sports feedback quality. To address the first problem, using rock climbing as our case study, we propose using auxiliary freely-available web data from the target domain, such as competition videos and coaching manuals, in addition to existing sports feedback from a disjoint, source domain to improve sports feedback generation performance on the target domain. To improve evaluation, we propose two evaluation metrics: (1) specificity and (2) actionability. Together, our approach enables more meaningful and practical generation of sports feedback under limited annotations.

### 🤖 AI 总结

**一句话总结**：While there is rapid progress in video-LLMs with advanced reasoning capabilities, prior work shows that these models struggle on the challenging task of sports feedback generation and require expensiv...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：LLMs with advanced reasoning capabilities, fail to capture the unique aspects of sports feedback quality. To address the first problem, available web data from the target domain, source domain to improve sports feedback generation performance on the target domain. To improve evaluation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.08996v1) | [下载PDF](https://arxiv.org/pdf/2602.08996v1.pdf)

---

## [14. WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models](https://arxiv.org/abs/2602.08971v1)

**作者**：Yu Shang, Zhuohang Li, Yiding Ma 等 19 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-02-09

### 📄 论文摘要

While world models have emerged as a cornerstone of embodied intelligence by enabling agents to reason about environmental dynamics through action-conditioned prediction, their evaluation remains fragmented. Current evaluation of embodied world models has largely focused on perceptual fidelity (e.g., video generation quality), overlooking the functional utility of these models in downstream decision-making tasks. In this work, we introduce WorldArena, a unified benchmark designed to systematically evaluate embodied world models across both perceptual and functional dimensions. WorldArena assesses models through three dimensions: video perception quality, measured with 16 metrics across six sub-dimensions; embodied task functionality, which evaluates world models as data engines, policy evaluators, and action planners integrating with subjective human evaluation. Furthermore, we propose EWMScore, a holistic metric integrating multi-dimensional performance into a single interpretable index. Through extensive experiments on 14 representative models, we reveal a significant perception-functionality gap, showing that high visual quality does not necessarily translate into strong embodied task capability. WorldArena benchmark with the public leaderboard is released at https://worldarena.ai, providing a framework for tracking progress toward truly functional world models in embodied AI.

### 🤖 AI 总结

**一句话总结**：While world models have emerged as a cornerstone of embodied intelligence by enabling agents to reason about environmental dynamics through action-conditioned prediction, their evaluation remains frag...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：While world models have emerged as a cornerstone of embodied intelligence by enabling agents to reason about environmental dynamics through action, their evaluation remains fragmented. Current evaluation of embodied world models has largely focused on perceptual fidelity (e.g., showing that high visual quality does not necessarily translate into strong embodied task capability. WorldArena benchmark with the public leaderboard is released at https://worldarena.ai, providing a framework for tracking progress toward truly functional world models in embodied AI.

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.08971v1) | [下载PDF](https://arxiv.org/pdf/2602.08971v1.pdf)

---

## [15. Modeling 3D Pedestrian-Vehicle Interactions for Vehicle-Conditioned Pose Forecasting](https://arxiv.org/abs/2602.08962v1)

**作者**：Guangxun Zhu, Xuan Liu, Nicolas Pugeault 等 5 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-02-09

### 📄 论文摘要

Accurately predicting pedestrian motion is crucial for safe and reliable autonomous driving in complex urban environments. In this work, we present a 3D vehicle-conditioned pedestrian pose forecasting framework that explicitly incorporates surrounding vehicle information. To support this, we enhance the Waymo-3DSkelMo dataset with aligned 3D vehicle bounding boxes, enabling realistic modeling of multi-agent pedestrian-vehicle interactions. We introduce a sampling scheme to categorize scenes by pedestrian and vehicle count, facilitating training across varying interaction complexities. Our proposed network adapts the TBIFormer architecture with a dedicated vehicle encoder and pedestrian-vehicle interaction cross-attention module to fuse pedestrian and vehicle features, allowing predictions to be conditioned on both historical pedestrian motion and surrounding vehicles. Extensive experiments demonstrate substantial improvements in forecasting accuracy and validate different approaches for modeling pedestrian-vehicle interactions, highlighting the importance of vehicle-aware 3D pose prediction for autonomous driving. Code is available at: https://github.com/GuangxunZhu/VehCondPose3D

### 🤖 AI 总结

**一句话总结**：Accurately predicting pedestrian motion is crucial for safe and reliable autonomous driving in complex urban environments. In this work, we present a 3D vehicle-conditioned pedestrian pose forecasting...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：Accurately predicting pedestrian motion is crucial for safe and reliable autonomous driving in complex urban environments. In this work, agent pedestrian, facilitating training across varying interaction complexities. Our proposed network adapts the TBIFormer architecture with a dedicated vehicle encoder and pedestrian, aware 3D pose prediction for autonomous driving. Code is available at: https://github.com/GuangxunZhu/VehCondPose3D

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.08962v1) | [下载PDF](https://arxiv.org/pdf/2602.08962v1.pdf)

---

## [16. MotionCrafter: Dense Geometry and Motion Reconstruction with a 4D VAE](https://arxiv.org/abs/2602.08961v1)

**作者**：Ruijie Zhu, Jiahao Lu, Wenbo Hu 等 7 位作者  
**分类**：cs.CV, cs.AI, cs.CG, cs.LG  
**发布时间**：2026-02-09

### 📄 论文摘要

We introduce MotionCrafter, a video diffusion-based framework that jointly reconstructs 4D geometry and estimates dense motion from a monocular video. The core of our method is a novel joint representation of dense 3D point maps and 3D scene flows in a shared coordinate system, and a novel 4D VAE to effectively learn this representation. Unlike prior work that forces the 3D value and latents to align strictly with RGB VAE latents-despite their fundamentally different distributions-we show that such alignment is unnecessary and leads to suboptimal performance. Instead, we introduce a new data normalization and VAE training strategy that better transfers diffusion priors and greatly improves reconstruction quality. Extensive experiments across multiple datasets demonstrate that MotionCrafter achieves state-of-the-art performance in both geometry reconstruction and dense scene flow estimation, delivering 38.64% and 25.0% improvements in geometry and motion reconstruction, respectively, all without any post-optimization. Project page: https://ruijiezhu94.github.io/MotionCrafter_Page

### 🤖 AI 总结

**一句话总结**：We introduce MotionCrafter, a video diffusion-based framework that jointly reconstructs 4D geometry and estimates dense motion from a monocular video. The core of our method is a novel joint represent...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：a video diffusion, we introduce a new data normalization and VAE training strategy that better transfers diffusion priors and greatly improves reconstruction quality. Extensive experiments across multiple datasets demonstrate that MotionCrafter achieves state

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.08961v1) | [下载PDF](https://arxiv.org/pdf/2602.08961v1.pdf)

---

## [17. Grow with the Flow: 4D Reconstruction of Growing Plants with Gaussian Flow Fields](https://arxiv.org/abs/2602.08958v1)

**作者**：Weihan Luo, Lily Goli, Sherwin Bahmani 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-09

### 📄 论文摘要

Modeling the time-varying 3D appearance of plants during their growth poses unique challenges: unlike many dynamic scenes, plants generate new geometry over time as they expand, branch, and differentiate. Recent motion modeling techniques are ill-suited to this problem setting. For example, deformation fields cannot introduce new geometry, and 4D Gaussian splatting constrains motion to a linear trajectory in space and time and cannot track the same set of Gaussians over time. Here, we introduce a 3D Gaussian flow field representation that models plant growth as a time-varying derivative over Gaussian parameters -- position, scale, orientation, color, and opacity -- enabling nonlinear and continuous-time growth dynamics. To initialize a sufficient set of Gaussian primitives, we reconstruct the mature plant and learn a process of reverse growth, effectively simulating the plant's developmental history in reverse. Our approach achieves superior image quality and geometric accuracy compared to prior methods on multi-view timelapse datasets of plant growth, providing a new approach for appearance modeling of growing 3D structures.

### 🤖 AI 总结

**一句话总结**：Modeling the time-varying 3D appearance of plants during their growth poses unique challenges: unlike many dynamic scenes, plants generate new geometry over time as they expand, branch, and differenti...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：and 4D Gaussian splatting constrains motion to a linear trajectory in space and time and cannot track the same set of Gaussians over time. Here

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.08958v1) | [下载PDF](https://arxiv.org/pdf/2602.08958v1.pdf)

---

## cs.LG

## [18. Next-Gen CAPTCHAs: Leveraging the Cognitive Gap for Scalable and Diverse GUI-Agent Defense](https://arxiv.org/abs/2602.09012v1)

**作者**：Jiacheng Liu, Yaxin Luo, Jiacheng Cui 等 6 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-02-09

### 📄 论文摘要

The rapid evolution of GUI-enabled agents has rendered traditional CAPTCHAs obsolete. While previous benchmarks like OpenCaptchaWorld established a baseline for evaluating multimodal agents, recent advancements in reasoning-heavy models, such as Gemini3-Pro-High and GPT-5.2-Xhigh have effectively collapsed this security barrier, achieving pass rates as high as 90% on complex logic puzzles like "Bingo". In response, we introduce Next-Gen CAPTCHAs, a scalable defense framework designed to secure the next-generation web against the advanced agents. Unlike static datasets, our benchmark is built upon a robust data generation pipeline, allowing for large-scale and easily scalable evaluations, notably, for backend-supported types, our system is capable of generating effectively unbounded CAPTCHA instances. We exploit the persistent human-agent "Cognitive Gap" in interactive perception, memory, decision-making, and action. By engineering dynamic tasks that require adaptive intuition rather than granular planning, we re-establish a robust distinction between biological users and artificial agents, offering a scalable and diverse defense mechanism for the agentic era.

### 🤖 AI 总结

**一句话总结**：The rapid evolution of GUI-enabled agents has rendered traditional CAPTCHAs obsolete. While previous benchmarks like OpenCaptchaWorld established a baseline for evaluating multimodal agents, recent ad...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：Gen CAPTCHAs: Leveraging the Cognitive Gap for Scalable and Diverse GUI, Agent Defense, enabled agents has rendered traditional CAPTCHAs obsolete. While previous benchmarks like OpenCaptchaWorld established a baseline for evaluating multimodal agents, High and GPT, generation web against the advanced agents. Unlike static datasets, agent "Cognitive Gap" in interactive perception, establish a robust distinction between biological users and artificial agents, offering a scalable and diverse defense mechanism for the agentic era.

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.09012v1) | [下载PDF](https://arxiv.org/pdf/2602.09012v1.pdf)

---

## [19. ANCRe: Adaptive Neural Connection Reassignment for Efficient Depth Scaling](https://arxiv.org/abs/2602.09009v1)

**作者**：Yilang Zhang, Bingcong Li, Niao He 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-09

### 📄 论文摘要

Scaling network depth has been a central driver behind the success of modern foundation models, yet recent investigations suggest that deep layers are often underutilized. This paper revisits the default mechanism for deepening neural networks, namely residual connections, from an optimization perspective. Rigorous analysis proves that the layout of residual connections can fundamentally shape convergence behavior, and even induces an exponential gap in convergence rates. Prompted by this insight, we introduce adaptive neural connection reassignment (ANCRe), a principled and lightweight framework that parameterizes and learns residual connectivities from the data. ANCRe adaptively reassigns residual connections with negligible computational and memory overhead ($<1\%$), while enabling more effective utilization of network depth. Extensive numerical tests across pre-training of large language models, diffusion models, and deep ResNets demonstrate consistently accelerated convergence, boosted performance, and enhanced depth efficiency over conventional residual connections.

### 🤖 AI 总结

**一句话总结**：Scaling network depth has been a central driver behind the success of modern foundation models, yet recent investigations suggest that deep layers are often underutilized. This paper revisits the defa...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：yet recent investigations suggest that deep layers are often underutilized. This paper revisits the default mechanism for deepening neural networks, training of large language models, diffusion models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.09009v1) | [下载PDF](https://arxiv.org/pdf/2602.09009v1.pdf)

---

## [20. ShapeCond: Fast Shapelet-Guided Dataset Condensation for Time Series Classification](https://arxiv.org/abs/2602.09008v1)

**作者**：Sijia Peng, Yun Xiong, Xi Chen 等 8 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-09

### 📄 论文摘要

Time series data supports many domains (e.g., finance and climate science), but its rapid growth strains storage and computation. Dataset condensation can alleviate this by synthesizing a compact training set that preserves key information. Yet most condensation methods are image-centric and often fail on time series because they miss time-series-specific temporal structure, especially local discriminative motifs such as shapelets. In this work, we propose ShapeCond, a novel and efficient condensation framework for time series classification that leverages shapelet-based dataset knowledge via a shapelet-guided optimization strategy. Our shapelet-assisted synthesis cost is independent of sequence length: longer series yield larger speedups in synthesis (e.g., 29$\times$ faster over prior state-of-the-art method CondTSC for time-series condensation, and up to 10,000$\times$ over naively using shapelets on the Sleep dataset with 3,000 timesteps). By explicitly preserving critical local patterns, ShapeCond improves downstream accuracy and consistently outperforms all prior state-of-the-art time series dataset condensation methods across extensive experiments. Code is available at https://github.com/lunaaa95/ShapeCond.

### 🤖 AI 总结

**一句话总结**：Time series data supports many domains (e.g., finance and climate science), but its rapid growth strains storage and computation. Dataset condensation can alleviate this by synthesizing a compact trai...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：Time series data supports many domains (e.g., but its rapid growth strains storage and computation. Dataset condensation can alleviate this by synthesizing a compact training set that preserves key information. Yet most condensation methods are image, centric and often fail on time series because they miss time, a novel and efficient condensation framework for time series classification that leverages shapelet, 000$\times$ over naively using shapelets on the Sleep dataset with 3, art time series dataset condensation methods across extensive experiments. Code is available at https://github.com/lunaaa95/ShapeCond.

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.09008v1) | [下载PDF](https://arxiv.org/pdf/2602.09008v1.pdf)

---

## [21. ARO: A New Lens On Matrix Optimization For Large Models](https://arxiv.org/abs/2602.09006v1)

**作者**：Wenbo Gong, Javier Zazo, Qijun Luo 等 6 位作者  
**分类**：cs.LG, cs.AI, math.OC  
**发布时间**：2026-02-09

### 📄 论文摘要

Matrix-based optimizers have attracted growing interest for improving LLM training efficiency, with significant progress centered on orthogonalization/whitening based methods. While yielding substantial performance gains, a fundamental question arises: can we develop new paradigms beyond orthogonalization, pushing the efficiency frontier further? We present \textbf{Adaptively Rotated Optimization (ARO}, a new matrix optimization framework that treats gradient rotation as a first class design principle. ARO accelerates LLM training by performing normed steepest descent in a rotated coordinate system, where the rotation is determined by a novel norm-informed policy. This perspective yields update rules that go beyond existing orthogonalization and whitening optimizers, improving sample efficiency in practice. To make comparisons reliable, we propose a rigorously controlled benchmarking protocol that reduces confounding and bias. Under this protocol, ARO consistently outperforms AdamW (by 1.3 $\sim$1.35$\times$) and orthogonalization methods (by 1.1$\sim$1.15$\times$) in LLM pretraining at up to 8B activated parameters, and up to $8\times$ overtrain budget, without evidence of diminishing returns. Finally, we discuss how ARO can be reformulated as a symmetry-aware optimizer grounded in rotational symmetries of residual streams, motivating advanced designs that enable computationally efficient exploitation of cross-layer/cross module couplings.

### 🤖 AI 总结

**一句话总结**：Matrix-based optimizers have attracted growing interest for improving LLM training efficiency, with significant progress centered on orthogonalization/whitening based methods. While yielding substanti...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：based optimizers have attracted growing interest for improving LLM training efficiency, with significant progress centered on orthogonalization/whitening based methods. While yielding substantial performance gains, a new matrix optimization framework that treats gradient rotation as a first class design principle. ARO accelerates LLM training by performing normed steepest descent in a rotated coordinate system, ARO consistently outperforms AdamW (by 1.3 $\sim$1.35$\times$) and orthogonalization methods (by 1.1$\sim$1.15$\times$) in LLM pretraining at up to 8B activated parameters, and up to $8\times$ overtrain budget

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.09006v1) | [下载PDF](https://arxiv.org/pdf/2602.09006v1.pdf)

---

## [22. DirMoE: Dirichlet-routed Mixture of Experts](https://arxiv.org/abs/2602.09001v1)

**作者**：Amirhossein Vahidi, Hesam Asadollahzadeh, Navid Akhavan Attar 等 7 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-09

### 📄 论文摘要

Mixture-of-Experts (MoE) models have demonstrated exceptional performance in large-scale language models. Existing routers typically rely on non-differentiable Top-$k$+Softmax, limiting their performance and scalability. We argue that two distinct decisions, which experts to activate and how to distribute expert contributions among them, are conflated in standard Top-$k$+Softmax. We introduce Dirichlet-Routed MoE (DirMoE), a novel end-to-end differentiable routing mechanism built on a Dirichlet variational autoencoder framework. This design fundamentally disentangles the core routing problems: expert selection, modeled by a Bernoulli component, and expert contribution among chosen experts, handled by a Dirichlet component. The entire forward pass remains fully differentiable through the use of Gumbel-Sigmoid relaxation for the expert selection and implicit reparameterization for the Dirichlet distribution. Our training objective, a variational ELBO, includes a direct sparsity penalty that precisely controls the number of active experts in expectation, alongside a schedule for key hyperparameters that guides the model from an exploratory to a definitive routing state. Moreover, our DirMoE router matches or exceeds other methods while improving expert specialization.

### 🤖 AI 总结

**一句话总结**：Mixture-of-Experts (MoE) models have demonstrated exceptional performance in large-scale language models. Existing routers typically rely on non-differentiable Top-$k$+Softmax, limiting their performa...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：handled by a Dirichlet component. The entire forward pass remains fully differentiable through the use of Gumbel, Sigmoid relaxation for the expert selection and implicit reparameterization for the Dirichlet distribution. Our training objective

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.09001v1) | [下载PDF](https://arxiv.org/pdf/2602.09001v1.pdf)

---

## [23. Improving Detection of Rare Nodes in Hierarchical Multi-Label Learning](https://arxiv.org/abs/2602.08986v1)

**作者**：Isaac Xu, Martin Gillis, Ayushi Sharma 等 6 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-09

### 📄 论文摘要

In hierarchical multi-label classification, a persistent challenge is enabling model predictions to reach deeper levels of the hierarchy for more detailed or fine-grained classifications. This difficulty partly arises from the natural rarity of certain classes (or hierarchical nodes) and the hierarchical constraint that ensures child nodes are almost always less frequent than their parents. To address this, we propose a weighted loss objective for neural networks that combines node-wise imbalance weighting with focal weighting components, the latter leveraging modern quantification of ensemble uncertainties. By emphasizing rare nodes rather than rare observations (data points), and focusing on uncertain nodes for each model output distribution during training, we observe improvements in recall by up to a factor of five on benchmark datasets, along with statistically significant gains in $F_{1}$ score. We also show our approach aids convolutional networks on challenging tasks, as in situations with suboptimal encoders or limited data.

### 🤖 AI 总结

**一句话总结**：In hierarchical multi-label classification, a persistent challenge is enabling model predictions to reach deeper levels of the hierarchy for more detailed or fine-grained classifications. This difficu...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：a persistent challenge is enabling model predictions to reach deeper levels of the hierarchy for more detailed or fine, grained classifications. This difficulty partly arises from the natural rarity of certain classes (or hierarchical nodes) and the hierarchical constraint that ensures child nodes are almost always less frequent than their parents. To address this, we propose a weighted loss objective for neural networks that combines node, the latter leveraging modern quantification of ensemble uncertainties. By emphasizing rare nodes rather than rare observations (data points), and focusing on uncertain nodes for each model output distribution during training, along with statistically significant gains in $F_{1}$ score. We also show our approach aids convolutional networks on challenging tasks

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.08986v1) | [下载PDF](https://arxiv.org/pdf/2602.08986v1.pdf)

---

## [24. StretchTime: Adaptive Time Series Forecasting via Symplectic Attention](https://arxiv.org/abs/2602.08983v1)

**作者**：Yubin Kim, Viresh Pati, Jevon Twitty 等 6 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-09

### 📄 论文摘要

Transformer architectures have established strong baselines in time series forecasting, yet they typically rely on positional encodings that assume uniform, index-based temporal progression. However, real-world systems, from shifting financial cycles to elastic biological rhythms, frequently exhibit "time-warped" dynamics where the effective flow of time decouples from the sampling index. In this work, we first formalize this misalignment and prove that rotary position embedding (RoPE) is mathematically incapable of representing non-affine temporal warping. To address this, we propose Symplectic Positional Embeddings (SyPE), a learnable encoding framework derived from Hamiltonian mechanics. SyPE strictly generalizes RoPE by extending the rotation group $\mathrm{SO}(2)$ to the symplectic group $\mathrm{Sp}(2,\mathbb{R})$, modulated by a novel input-dependent adaptive warp module. By allowing the attention mechanism to adaptively dilate or contract temporal coordinates end-to-end, our approach captures locally varying periodicities without requiring pre-defined warping functions. We implement this mechanism in StretchTime, a multivariate forecasting architecture that achieves state-of-the-art performance on standard benchmarks, demonstrating superior robustness on datasets exhibiting non-stationary temporal dynamics.

### 🤖 AI 总结

**一句话总结**：Transformer architectures have established strong baselines in time series forecasting, yet they typically rely on positional encodings that assume uniform, index-based temporal progression. However, ...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：Transformer architectures have established strong baselines in time series forecasting, we first formalize this misalignment and prove that rotary position embedding (RoPE) is mathematically incapable of representing non, we propose Symplectic Positional Embeddings (SyPE)

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.08983v1) | [下载PDF](https://arxiv.org/pdf/2602.08983v1.pdf)

---

## [25. Distributionally Robust Optimization via Generative Ambiguity Modeling](https://arxiv.org/abs/2602.08976v1)

**作者**：Jiaqi Wen, Jianyi Yang  
**分类**：cs.LG  
**发布时间**：2026-02-09

### 📄 论文摘要

This paper studies Distributionally Robust Optimization (DRO), a fundamental framework for enhancing the robustness and generalization of statistical learning and optimization. An effective ambiguity set for DRO must involve distributions that remain consistent to the nominal distribution while being diverse enough to account for a variety of potential scenarios. Moreover, it should lead to tractable DRO solutions. To this end, we propose generative model-based ambiguity sets that capture various adversarial distributions beyond the nominal support space while maintaining consistency with the nominal distribution. Building on this generative ambiguity modeling, we propose DRO with Generative Ambiguity Set (GAS-DRO), a tractable DRO algorithm that solves the inner maximization over the parameterized generative model space. We formally establish the stationary convergence performance of GAS-DRO. We implement GAS-DRO with a diffusion model and empirically demonstrate its superior Out-of-Distribution (OOD) generalization performance in ML tasks.

### 🤖 AI 总结

**一句话总结**：This paper studies Distributionally Robust Optimization (DRO), a fundamental framework for enhancing the robustness and generalization of statistical learning and optimization. An effective ambiguity ...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：Distributionally Robust Optimization via Generative Ambiguity Modeling, a fundamental framework for enhancing the robustness and generalization of statistical learning and optimization. An effective ambiguity set for DRO must involve distributions that remain consistent to the nominal distribution while being diverse enough to account for a variety of potential scenarios. Moreover, we propose generative model, based ambiguity sets that capture various adversarial distributions beyond the nominal support space while maintaining consistency with the nominal distribution. Building on this generative ambiguity modeling, we propose DRO with Generative Ambiguity Set (GAS, a tractable DRO algorithm that solves the inner maximization over the parameterized generative model space. We formally establish the stationary convergence performance of GAS, DRO with a diffusion model and empirically demonstrate its superior Out, Distribution (OOD) generalization performance in ML tasks.

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.08976v1) | [下载PDF](https://arxiv.org/pdf/2602.08976v1.pdf)

---

## [26. A Behavioural and Representational Evaluation of Goal-Directedness in Language Model Agents](https://arxiv.org/abs/2602.08964v1)

**作者**：Raghu Arghal, Fade Chen, Niall Dalton 等 9 位作者  
**分类**：cs.LG, cs.AI, cs.CL, cs.CY  
**发布时间**：2026-02-09

### 📄 论文摘要

Understanding an agent's goals helps explain and predict its behaviour, yet there is no established methodology for reliably attributing goals to agentic systems. We propose a framework for evaluating goal-directedness that integrates behavioural evaluation with interpretability-based analyses of models' internal representations. As a case study, we examine an LLM agent navigating a 2D grid world toward a goal state. Behaviourally, we evaluate the agent against an optimal policy across varying grid sizes, obstacle densities, and goal structures, finding that performance scales with task difficulty while remaining robust to difficulty-preserving transformations and complex goal structures. We then use probing methods to decode the agent's internal representations of the environment state and its multi-step action plans. We find that the LLM agent non-linearly encodes a coarse spatial map of the environment, preserving approximate task-relevant cues about its position and the goal location; that its actions are broadly consistent with these internal representations; and that reasoning reorganises them, shifting from broader environment structural cues toward information supporting immediate action selection. Our findings support the view that introspective examination is required beyond behavioural evaluations to characterise how agents represent and pursue their objectives.

### 🤖 AI 总结

**一句话总结**：Understanding an agent's goals helps explain and predict its behaviour, yet there is no established methodology for reliably attributing goals to agentic systems. We propose a framework for evaluating...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：Directedness in Language Model Agents, Understanding an agent's goals helps explain and predict its behaviour, yet there is no established methodology for reliably attributing goals to agentic systems. We propose a framework for evaluating goal, we examine an LLM agent navigating a 2D grid world toward a goal state. Behaviourally, we evaluate the agent against an optimal policy across varying grid sizes, finding that performance scales with task difficulty while remaining robust to difficulty, preserving transformations and complex goal structures. We then use probing methods to decode the agent's internal representations of the environment state and its multi, step action plans. We find that the LLM agent non, shifting from broader environment structural cues toward information supporting immediate action selection. Our findings support the view that introspective examination is required beyond behavioural evaluations to characterise how agents represent and pursue their objectives.

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.08964v1) | [下载PDF](https://arxiv.org/pdf/2602.08964v1.pdf)

---

## [27. StealthRL: Reinforcement Learning Paraphrase Attacks for Multi-Detector Evasion of AI-Text Detectors](https://arxiv.org/abs/2602.08934v1)

**作者**：Suraj Ranganath, Atharv Ramesh  
**分类**：cs.LG, cs.AI, cs.CR  
**发布时间**：2026-02-09

### 📄 论文摘要

AI-text detectors face a critical robustness challenge: adversarial paraphrasing attacks that preserve semantics while evading detection. We introduce StealthRL, a reinforcement learning framework that stress-tests detector robustness under realistic adversarial conditions. StealthRL trains a paraphrase policy against a multi-detector ensemble using Group Relative Policy Optimization (GRPO) with LoRA adapters on Qwen3-4B, optimizing a composite reward that balances detector evasion with semantic preservation. We evaluate six attack settings (M0-M5) against three detector families (RoBERTa, FastDetectGPT, and Binoculars) at the security-relevant 1% false positive rate operating point. StealthRL achieves near-zero detection (0.001 mean TPR@1%FPR), reduces mean AUROC from 0.74 to 0.27, and attains a 99.9% attack success rate. Critically, attacks transfer to a held-out detector family not seen during training, revealing shared architectural vulnerabilities rather than detector-specific brittleness. We additionally conduct LLM-based quality evaluation via Likert scoring, analyze detector score distributions to explain why evasion succeeds, and provide per-detector AUROC with bootstrap confidence intervals. Our results expose significant robustness gaps in current AI-text detection and establish StealthRL as a principled adversarial evaluation protocol. Code and evaluation pipeline are publicly available at https://github.com/suraj-ranganath/StealthRL.

### 🤖 AI 总结

**一句话总结**：AI-text detectors face a critical robustness challenge: adversarial paraphrasing attacks that preserve semantics while evading detection. We introduce StealthRL, a reinforcement learning framework tha...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：Detector Evasion of AI, tests detector robustness under realistic adversarial conditions. StealthRL trains a paraphrase policy against a multi, M5) against three detector families (RoBERTa, FastDetectGPT, and attains a 99.9% attack success rate. Critically, out detector family not seen during training, specific brittleness. We additionally conduct LLM, analyze detector score distributions to explain why evasion succeeds, detector AUROC with bootstrap confidence intervals. Our results expose significant robustness gaps in current AI, text detection and establish StealthRL as a principled adversarial evaluation protocol. Code and evaluation pipeline are publicly available at https://github.com/suraj

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.08934v1) | [下载PDF](https://arxiv.org/pdf/2602.08934v1.pdf)

---

## [28. DynamiQ: Accelerating Gradient Synchronization using Compressed Multi-hop All-reduce](https://arxiv.org/abs/2602.08923v1)

**作者**：Wenchen Han, Shay Vargaftik, Michael Mitzenmacher 等 4 位作者  
**分类**：cs.LG, cs.DC, cs.NI  
**发布时间**：2026-02-09

### 📄 论文摘要

Multi-hop all-reduce is the de facto backbone of large model training. As the training scale increases, the network often becomes a bottleneck, motivating reducing the volume of transmitted data. Accordingly, recent systems demonstrated significant acceleration of the training process using gradient quantization. However, these systems are not optimized for multi-hop aggregation, where entries are partially summed multiple times along their aggregation topology.   This paper presents DynamiQ, a quantization framework that bridges the gap between quantization best practices and multi-hop aggregation. DynamiQ introduces novel techniques to better represent partial sums, co-designed with a decompress-accumulate-recompress fused kernel to facilitate fast execution.   We extended PyTorch DDP to support DynamiQ over NCCL P2P, and across different LLMs, tasks, and scales, we demonstrate consistent improvement of up to 34.2% over the best among state-of-the-art methods such as Omni-Reduce, THC, and emerging standards such as MXFP4, MXFP6, and MXFP8. Further, DynamiQ is the only evaluated method that consistently reaches near-baseline accuracy (e.g., 99.9% of the BF16 baseline) and does so while significantly accelerating the training.

### 🤖 AI 总结

**一句话总结**：Multi-hop all-reduce is the de facto backbone of large model training. As the training scale increases, the network often becomes a bottleneck, motivating reducing the volume of transmitted data. Acco...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：reduce is the de facto backbone of large model training. As the training scale increases, recent systems demonstrated significant acceleration of the training process using gradient quantization. However, and across different LLMs, 99.9% of the BF16 baseline) and does so while significantly accelerating the training.

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.08923v1) | [下载PDF](https://arxiv.org/pdf/2602.08923v1.pdf)

---

## [29. Diffusion-Inspired Reconfiguration of Transformers for Uncertainty Calibration](https://arxiv.org/abs/2602.08920v1)

**作者**：Manh Cuong Dao, Quang Hung Pham, Phi Le Nguyen 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-09

### 📄 论文摘要

Uncertainty calibration in pre-trained transformers is critical for their reliable deployment in risk-sensitive applications. Yet, most existing pre-trained transformers do not have a principled mechanism for uncertainty propagation through their feature transformation stack. In this work, we propose a diffusion-inspired reconfiguration of transformers in which each feature transformation block is modeled as a probabilistic mapping. Composing these probabilistic mappings reveals a probability path that mimics the structure of a diffusion process, transporting data mass from the input distribution to the pre-trained feature distribution. This probability path can then be recompiled on a diffusion process with a unified transition model to enable principled propagation of representation uncertainty throughout the pre-trained model's architecture while maintaining its original predictive performance. Empirical results across a variety of vision and language benchmarks demonstrate that our method achieves superior calibration and predictive accuracy compared to existing uncertainty-aware transformers.

### 🤖 AI 总结

**一句话总结**：Uncertainty calibration in pre-trained transformers is critical for their reliable deployment in risk-sensitive applications. Yet, most existing pre-trained transformers do not have a principled mecha...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：Diffusion, Inspired Reconfiguration of Transformers for Uncertainty Calibration, Uncertainty calibration in pre, trained transformers is critical for their reliable deployment in risk, trained transformers do not have a principled mechanism for uncertainty propagation through their feature transformation stack. In this work, we propose a diffusion, inspired reconfiguration of transformers in which each feature transformation block is modeled as a probabilistic mapping. Composing these probabilistic mappings reveals a probability path that mimics the structure of a diffusion process, trained feature distribution. This probability path can then be recompiled on a diffusion process with a unified transition model to enable principled propagation of representation uncertainty throughout the pre, trained model's architecture while maintaining its original predictive performance. Empirical results across a variety of vision and language benchmarks demonstrate that our method achieves superior calibration and predictive accuracy compared to existing uncertainty, aware transformers.

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.08920v1) | [下载PDF](https://arxiv.org/pdf/2602.08920v1.pdf)

---

## [30. GEMSS: A Variational Bayesian Method for Discovering Multiple Sparse Solutions in Classification and Regression Problems](https://arxiv.org/abs/2602.08913v1)

**作者**：Kateřina Henclová, Václav Šmídl  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-02-09

### 📄 论文摘要

Selecting interpretable feature sets in underdetermined ($n \ll p$) and highly correlated regimes constitutes a fundamental challenge in data science, particularly when analyzing physical measurements. In such settings, multiple distinct sparse subsets may explain the response equally well. Identifying these alternatives is crucial for generating domain-specific insights into the underlying mechanisms, yet conventional methods typically isolate a single solution, obscuring the full spectrum of plausible explanations.   We present GEMSS (Gaussian Ensemble for Multiple Sparse Solutions), a variational Bayesian framework specifically designed to simultaneously discover multiple, diverse sparse feature combinations. The method employs a structured spike-and-slab prior for sparsity, a mixture of Gaussians to approximate the intractable multimodal posterior, and a Jaccard-based penalty to further control solution diversity. Unlike sequential greedy approaches, GEMSS optimizes the entire ensemble of solutions within a single objective function via stochastic gradient descent.   The method is validated on a comprehensive benchmark comprising 128 synthetic experiments across classification and regression tasks. Results demonstrate that GEMSS scales effectively to high-dimensional settings ($p=5000$) with sample size as small as $n = 50$, generalizes seamlessly to continuous targets, handles missing data natively, and exhibits remarkable robustness to class imbalance and Gaussian noise.   GEMSS is available as a Python package 'gemss' at PyPI. The full GitHub repository at https://github.com/kat-er-ina/gemss/ also includes a free, easy-to-use application suitable for non-coders.

### 🤖 AI 总结

**一句话总结**：Selecting interpretable feature sets in underdetermined ($n \ll p$) and highly correlated regimes constitutes a fundamental challenge in data science, particularly when analyzing physical measurements...

**研究动机**：AI服务不可用

**核心方法**：AI服务不可用

**主要结论**：AI服务不可用

**关键词**：multiple distinct sparse subsets may explain the response equally well. Identifying these alternatives is crucial for generating domain, generalizes seamlessly to continuous targets, and exhibits remarkable robustness to class imbalance and Gaussian noise.   GEMSS is available as a Python package 'gemss' at PyPI. The full GitHub repository at https://github.com/kat

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.08913v1) | [下载PDF](https://arxiv.org/pdf/2602.08913v1.pdf)

---

