# arXiv AI 论文日报 | 2026-02-12

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (8 篇)
- [cs.LG](#csLG) (14 篇)
- [cs.AI](#csAI) (1 篇)
- [cs.CL](#csCL) (7 篇)

---

## cs.AI

## [1. FormalJudge: A Neuro-Symbolic Paradigm for Agentic Oversight](https://arxiv.org/abs/2602.11136v1)

**作者**：Jiayi Zhou, Yang Sheng, Hantao Lou 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-11

### 📄 论文摘要

As LLM-based agents increasingly operate in high-stakes domains with real-world consequences, ensuring their behavioral safety becomes paramount. The dominant oversight paradigm, LLM-as-a-Judge, faces a fundamental dilemma: how can probabilistic systems reliably supervise other probabilistic systems without inheriting their failure modes? We argue that formal verification offers a principled escape from this dilemma, yet its adoption has been hindered by a critical bottleneck: the translation from natural language requirements to formal specifications. This paper bridges this gap by proposing , a neuro-symbolic framework that employs a bidirectional Formal-of-Thought architecture: LLMs serve as specification compilers that top-down decompose high-level human intent into atomic, verifiable constraints, then bottom-up prove compliance using Dafny specifications and Z3 Satisfiability modulo theories solving, which produces mathematical guarantees rather than probabilistic scores. We validate across three benchmarks spanning behavioral safety, multi-domain constraint adherence, and agentic upward deception detection. Experiments on 7 agent models demonstrate that achieves an average improvement of 16.6% over LLM-as-a-Judge baselines, enables weak-to-strong generalization where a 7B judge achieves over 90% accuracy detecting deception from 72B agents, and provides near-linear safety improvement through iterative refinement.

### 🤖 AI 总结

**一句话总结**：As LLM-based agents increasingly operate in high-stakes domains with real-world consequences, ensuring their behavioral safety becomes paramount. The dominant oversight paradigm, LLM-as-a-Judge, faces...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.11136v1) | [下载PDF](https://arxiv.org/pdf/2602.11136v1.pdf)

---

## cs.CL

## [2. TEGRA: Text Encoding With Graph and Retrieval Augmentation for Misinformation Detection](https://arxiv.org/abs/2602.11106v1)

**作者**：Géraud Faye, Wassila Ouerdane, Guillaume Gadek 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-02-11

### 📄 论文摘要

Misinformation detection is a critical task that can benefit significantly from the integration of external knowledge, much like manual fact-checking. In this work, we propose a novel method for representing textual documents that facilitates the incorporation of information from a knowledge base. Our approach, Text Encoding with Graph (TEG), processes documents by extracting structured information in the form of a graph and encoding both the text and the graph for classification purposes. Through extensive experiments, we demonstrate that this hybrid representation enhances misinformation detection performance compared to using language models alone. Furthermore, we introduce TEGRA, an extension of our framework that integrates domain-specific knowledge, further enhancing classification accuracy in most cases.

### 🤖 AI 总结

**一句话总结**：Misinformation detection is a critical task that can benefit significantly from the integration of external knowledge, much like manual fact-checking. In this work, we propose a novel method for repre...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2602.11106v1) | [下载PDF](https://arxiv.org/pdf/2602.11106v1.pdf)

---

## [3. Safety Recovery in Reasoning Models Is Only a Few Early Steering Steps Away](https://arxiv.org/abs/2602.11096v1)

**作者**：Soumya Suvra Ghosal, Souradip Chakraborty, Vaibhav Singh 等 6 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-02-11

### 📄 论文摘要

Reinforcement learning (RL) based post-training for explicit chain-of-thought (e.g., GRPO) improves the reasoning ability of multimodal large-scale reasoning models (MLRMs). But recent evidence shows that it can simultaneously degrade safety alignment and increase jailbreak success rates. We propose SafeThink, a lightweight inference-time defense that treats safety recovery as a satisficing constraint rather than a maximization objective. SafeThink monitors the evolving reasoning trace with a safety reward model and conditionally injects an optimized short corrective prefix ("Wait, think safely") only when the safety threshold is violated. In our evaluations across six open-source MLRMs and four jailbreak benchmarks (JailbreakV-28K, Hades, FigStep, and MM-SafetyBench), SafeThink reduces attack success rates by 30-60% (e.g., LlamaV-o1: 63.33% to 5.74% on JailbreakV-28K, R1-Onevision: 69.07% to 5.65% on Hades) while preserving reasoning performance (MathVista accuracy: 65.20% to 65.00%). A key empirical finding from our experiments is that safety recovery is often only a few steering steps away: intervening in the first 1-3 reasoning steps typically suffices to redirect the full generation toward safe completions.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning (RL) based post-training for explicit chain-of-thought (e.g., GRPO) improves the reasoning ability of multimodal large-scale reasoning models (MLRMs). But recent evidence shows ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.11096v1) | [下载PDF](https://arxiv.org/pdf/2602.11096v1.pdf)

---

## [4. Can Large Language Models Make Everyone Happy?](https://arxiv.org/abs/2602.11091v1)

**作者**：Usman Naseem, Gautam Siddharth Kashyap, Ebad Shabbir 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-02-11

### 📄 论文摘要

Misalignment in Large Language Models (LLMs) refers to the failure to simultaneously satisfy safety, value, and cultural dimensions, leading to behaviors that diverge from human expectations in real-world settings where these dimensions must co-occur. Existing benchmarks, such as SAFETUNEBED (safety-centric), VALUEBENCH (value-centric), and WORLDVIEW-BENCH (culture-centric), primarily evaluate these dimensions in isolation and therefore provide limited insight into their interactions and trade-offs. More recent efforts, including MIB and INTERPRETABILITY BENCHMARK-based on mechanistic interpretability, offer valuable perspectives on model failures; however, they remain insufficient for systematically characterizing cross-dimensional trade-offs. To address these gaps, we introduce MisAlign-Profile, a unified benchmark for measuring misalignment trade-offs inspired by mechanistic profiling. First, we construct MISALIGNTRADE, an English misaligned-aligned dataset across 112 normative domains taxonomies, including 14 safety, 56 value, and 42 cultural domains. In addition to domain labels, each prompt is classified with one of three orthogonal semantic types-object, attribute, or relations misalignment-using Gemma-2-9B-it and expanded via Qwen3-30B-A3B-Instruct-2507 with SimHash-based fingerprinting to avoid deduplication. Each prompt is paired with misaligned and aligned responses through two-stage rejection sampling to ensure quality. Second, we benchmark general-purpose, fine-tuned, and open-weight LLMs on MISALIGNTRADE-revealing 12%-34% misalignment trade-offs across dimensions.

### 🤖 AI 总结

**一句话总结**：Misalignment in Large Language Models (LLMs) refers to the failure to simultaneously satisfy safety, value, and cultural dimensions, leading to behaviors that diverge from human expectations in real-w...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.11091v1) | [下载PDF](https://arxiv.org/pdf/2602.11091v1.pdf)

---

## [5. DataChef: Cooking Up Optimal Data Recipes for LLM Adaptation via Reinforcement Learning](https://arxiv.org/abs/2602.11089v1)

**作者**：Yicheng Chen, Zerun Ma, Xinchen Xie 等 5 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-02-11

### 📄 论文摘要

In the current landscape of Large Language Models (LLMs), the curation of large-scale, high-quality training data is a primary driver of model performance. A key lever is the \emph{data recipe}, which comprises a data processing pipeline to transform raw sources into training corpora. Despite the growing use of LLMs to automate individual data processing steps, such as data synthesis and filtering, the overall design of data recipes remains largely manual and labor-intensive, requiring substantial human expertise and iteration. To bridge this gap, we formulate \emph{end-to-end data recipe generation} for LLM adaptation. Given a target benchmark and a pool of available data sources, a model is required to output a complete data recipe that adapts a base LLM to the target task. We present DataChef-32B, which performs online reinforcement learning using a proxy reward that predicts downstream performance for candidate recipes. Across six held-out tasks, DataChef-32B produces practical recipes that reach comparable downstream performance to those curated by human experts. Notably, the recipe from DataChef-32B adapts Qwen3-1.7B-Base to the math domain, achieving 66.7 on AIME'25 and surpassing Qwen3-1.7B. This work sheds new light on automating LLM training and developing self-evolving AI systems.

### 🤖 AI 总结

**一句话总结**：In the current landscape of Large Language Models (LLMs), the curation of large-scale, high-quality training data is a primary driver of model performance. A key lever is the \emph{data recipe}, which...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2602.11089v1) | [下载PDF](https://arxiv.org/pdf/2602.11089v1.pdf)

---

## [6. SteuerLLM: Local specialized large language model for German tax law analysis](https://arxiv.org/abs/2602.11081v1)

**作者**：Sebastian Wind, Jeta Sopa, Laurin Schmid 等 11 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-02-11

### 📄 论文摘要

Large language models (LLMs) demonstrate strong general reasoning and language understanding, yet their performance degrades in domains governed by strict formal rules, precise terminology, and legally binding structure. Tax law exemplifies these challenges, as correct answers require exact statutory citation, structured legal argumentation, and numerical accuracy under rigid grading schemes. We algorithmically generate SteuerEx, the first open benchmark derived from authentic German university tax law examinations. SteuerEx comprises 115 expert-validated examination questions spanning six core tax law domains and multiple academic levels, and employs a statement-level, partial-credit evaluation framework that closely mirrors real examination practice. We further present SteuerLLM, a domain-adapted LLM for German tax law trained on a large-scale synthetic dataset generated from authentic examination material using a controlled retrieval-augmented pipeline. SteuerLLM (28B parameters) consistently outperforms general-purpose instruction-tuned models of comparable size and, in several cases, substantially larger systems, demonstrating that domain-specific data and architectural adaptation are more decisive than parameter scale for performance on realistic legal reasoning tasks. All benchmark data, training datasets, model weights, and evaluation code are released openly to support reproducible research in domain-specific legal artificial intelligence. A web-based demo of SteuerLLM is available at https://steuerllm.i5.ai.fau.de.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) demonstrate strong general reasoning and language understanding, yet their performance degrades in domains governed by strict formal rules, precise terminology, and legall...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.11081v1) | [下载PDF](https://arxiv.org/pdf/2602.11081v1.pdf)

---

## [7. Simultaneous Speech-to-Speech Translation Without Aligned Data](https://arxiv.org/abs/2602.11072v1)

**作者**：Tom Labiausse, Romain Fabre, Yannick Estève 等 5 位作者  
**分类**：cs.CL, cs.SD, eess.AS  
**发布时间**：2026-02-11

### 📄 论文摘要

Simultaneous speech translation requires translating source speech into a target language in real-time while handling non-monotonic word dependencies. Traditional approaches rely on supervised training with word-level aligned data, which is difficult to collect at scale and thus depends on synthetic alignments using language-specific heuristics that are suboptimal. We propose Hibiki-Zero, which eliminates the need for word-level alignments entirely. This fundamentally simplifies the training pipeline and enables seamless scaling to diverse languages with varying grammatical structures, removing the bottleneck of designing language-specific alignment heuristics. We first train on sentence-level aligned data to learn speech translation at high latency, then apply a novel reinforcement learning strategy using GRPO to optimize latency while preserving translation quality. Hibiki-Zero achieves state-of-the-art performance in translation accuracy, latency, voice transfer, and naturalness across five X-to-English tasks. Moreover, we demonstrate that our model can be adapted to support a new input language with less than 1000h of speech. We provide examples, model weights, inference code and we release a benchmark containing 45h of multilingual data for speech translation evaluation.

### 🤖 AI 总结

**一句话总结**：Simultaneous speech translation requires translating source speech into a target language in real-time while handling non-monotonic word dependencies. Traditional approaches rely on supervised trainin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2602.11072v1) | [下载PDF](https://arxiv.org/pdf/2602.11072v1.pdf)

---

## [8. Conversational Behavior Modeling Foundation Model With Multi-Level Perception](https://arxiv.org/abs/2602.11065v1)

**作者**：Dingkun Zhou, Shuchang Pan, Jiachen Lian 等 14 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-02-11

### 📄 论文摘要

Human conversation is organized by an implicit chain of thoughts that manifests as timed speech acts. Capturing this perceptual pathway is key to building natural full-duplex interactive systems. We introduce a framework that models this process as multi-level perception, and then reasons over conversational behaviors via a Graph-of-Thoughts (GoT). Our approach formalizes the intent-to-action pathway with a hierarchical labeling scheme, predicting high-level communicative intents and low-level speech acts to learn their causal and temporal dependencies. To train this system, we develop a high quality corpus that pairs controllable, event-rich dialogue data with human-annotated labels. The GoT framework structures streaming predictions as an evolving graph, enabling a transformer to forecast the next speech act, generate concise justifications for its decisions, and dynamically refine its reasoning. Experiments on both synthetic and real duplex dialogues show that the framework delivers robust behavior detection, produces interpretable reasoning chains, and establishes a foundation for benchmarking conversational reasoning in full duplex spoken dialogue systems.

### 🤖 AI 总结

**一句话总结**：Human conversation is organized by an implicit chain of thoughts that manifests as timed speech acts. Capturing this perceptual pathway is key to building natural full-duplex interactive systems. We i...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：

**评分**：75

**论文链接**：[查看原文](https://arxiv.org/abs/2602.11065v1) | [下载PDF](https://arxiv.org/pdf/2602.11065v1.pdf)

---

## cs.CV

## [9. SurfPhase: 3D Interfacial Dynamics in Two-Phase Flows from Sparse Videos](https://arxiv.org/abs/2602.11154v1)

**作者**：Yue Gao, Hong-Xing Yu, Sanghyeon Chang 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-11

### 📄 论文摘要

Interfacial dynamics in two-phase flows govern momentum, heat, and mass transfer, yet remain difficult to measure experimentally. Classical techniques face intrinsic limitations near moving interfaces, while existing neural rendering methods target single-phase flows with diffuse boundaries and cannot handle sharp, deformable liquid-vapor interfaces. We propose SurfPhase, a novel model for reconstructing 3D interfacial dynamics from sparse camera views. Our approach integrates dynamic Gaussian surfels with a signed distance function formulation for geometric consistency, and leverages a video diffusion model to synthesize novel-view videos to refine reconstruction from sparse observations. We evaluate on a new dataset of high-speed pool boiling videos, demonstrating high-quality view synthesis and velocity estimation from only two camera views. Project website: https://yuegao.me/SurfPhase.

### 🤖 AI 总结

**一句话总结**：Interfacial dynamics in two-phase flows govern momentum, heat, and mass transfer, yet remain difficult to measure experimentally. Classical techniques face intrinsic limitations near moving interfaces...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：

**评分**：60

**论文链接**：[查看原文](https://arxiv.org/abs/2602.11154v1) | [下载PDF](https://arxiv.org/pdf/2602.11154v1.pdf)

---

## [10. Beyond VLM-Based Rewards: Diffusion-Native Latent Reward Modeling](https://arxiv.org/abs/2602.11146v1)

**作者**：Gongye Liu, Bo Yang, Yida Zhi 等 11 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-02-11

### 📄 论文摘要

Preference optimization for diffusion and flow-matching models relies on reward functions that are both discriminatively robust and computationally efficient. Vision-Language Models (VLMs) have emerged as the primary reward provider, leveraging their rich multimodal priors to guide alignment. However, their computation and memory cost can be substantial, and optimizing a latent diffusion generator through a pixel-space reward introduces a domain mismatch that complicates alignment. In this paper, we propose DiNa-LRM, a diffusion-native latent reward model that formulates preference learning directly on noisy diffusion states. Our method introduces a noise-calibrated Thurstone likelihood with diffusion-noise-dependent uncertainty. DiNa-LRM leverages a pretrained latent diffusion backbone with a timestep-conditioned reward head, and supports inference-time noise ensembling, providing a diffusion-native mechanism for test-time scaling and robust rewarding. Across image alignment benchmarks, DiNa-LRM substantially outperforms existing diffusion-based reward baselines and achieves performance competitive with state-of-the-art VLMs at a fraction of the computational cost. In preference optimization, we demonstrate that DiNa-LRM improves preference optimization dynamics, enabling faster and more resource-efficient model alignment.

### 🤖 AI 总结

**一句话总结**：Preference optimization for diffusion and flow-matching models relies on reward functions that are both discriminatively robust and computationally efficient. Vision-Language Models (VLMs) have emerge...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：

**评分**：73

**论文链接**：[查看原文](https://arxiv.org/abs/2602.11146v1) | [下载PDF](https://arxiv.org/pdf/2602.11146v1.pdf)

---

## [11. PhyCritic: Multimodal Critic Models for Physical AI](https://arxiv.org/abs/2602.11124v1)

**作者**：Tianyi Xiong, Shihao Wang, Guilin Liu 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-11

### 📄 论文摘要

With the rapid development of large multimodal models, reliable judge and critic models have become essential for open-ended evaluation and preference alignment, providing pairwise preferences, numerical scores, and explanatory justifications for assessing model-generated responses. However, existing critics are primarily trained in general visual domains such as captioning or image question answering, leaving physical AI tasks involving perception, causal reasoning, and planning largely underexplored. We introduce PhyCritic, a multimodal critic model optimized for physical AI through a two-stage RLVR pipeline: a physical skill warmup stage that enhances physically oriented perception and reasoning, followed by self-referential critic finetuning, where the critic generates its own prediction as an internal reference before judging candidate responses, improving judgment stability and physical correctness. Across both physical and general-purpose multimodal judge benchmarks, PhyCritic achieves strong performance gains over open-source baselines and, when applied as a policy model, further improves perception and reasoning in physically grounded tasks.

### 🤖 AI 总结

**一句话总结**：With the rapid development of large multimodal models, reliable judge and critic models have become essential for open-ended evaluation and preference alignment, providing pairwise preferences, numeri...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.11124v1) | [下载PDF](https://arxiv.org/pdf/2602.11124v1.pdf)

---

## [12. HairWeaver: Few-Shot Photorealistic Hair Motion Synthesis with Sim-to-Real Guided Video Diffusion](https://arxiv.org/abs/2602.11117v1)

**作者**：Di Chang, Ji Hou, Aljaz Bozic 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-11

### 📄 论文摘要

We present HairWeaver, a diffusion-based pipeline that animates a single human image with realistic and expressive hair dynamics. While existing methods successfully control body pose, they lack specific control over hair, and as a result, fail to capture the intricate hair motions, resulting in stiff and unrealistic animations. HairWeaver overcomes this limitation using two specialized modules: a Motion-Context-LoRA to integrate motion conditions and a Sim2Real-Domain-LoRA to preserve the subject's photoreal appearance across different data domains. These lightweight components are designed to guide a video diffusion backbone while maintaining its core generative capabilities. By training on a specialized dataset of dynamic human motion generated from a CG simulator, HairWeaver affords fine control over hair motion and ultimately learns to produce highly realistic hair that responds naturally to movement. Comprehensive evaluations demonstrate that our approach sets a new state of the art, producing lifelike human hair animations with dynamic details.

### 🤖 AI 总结

**一句话总结**：We present HairWeaver, a diffusion-based pipeline that animates a single human image with realistic and expressive hair dynamics. While existing methods successfully control body pose, they lack speci...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.11117v1) | [下载PDF](https://arxiv.org/pdf/2602.11117v1.pdf)

---

## [13. FastFlow: Accelerating The Generative Flow Matching Models with Bandit Inference](https://arxiv.org/abs/2602.11105v1)

**作者**：Divya Jyoti Bajpai, Dhruv Bhardwaj, Soumya Roy 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-11

### 📄 论文摘要

Flow-matching models deliver state-of-the-art fidelity in image and video generation, but the inherent sequential denoising process renders them slower. Existing acceleration methods like distillation, trajectory truncation, and consistency approaches are static, require retraining, and often fail to generalize across tasks. We propose FastFlow, a plug-and-play adaptive inference framework that accelerates generation in flow matching models. FastFlow identifies denoising steps that produce only minor adjustments to the denoising path and approximates them without using the full neural network models used for velocity predictions. The approximation utilizes finite-difference velocity estimates from prior predictions to efficiently extrapolate future states, enabling faster advancements along the denoising path at zero compute cost. This enables skipping computation at intermediary steps. We model the decision of how many steps to safely skip before requiring a full model computation as a multi-armed bandit problem. The bandit learns the optimal skips to balance speed with performance. FastFlow integrates seamlessly with existing pipelines and generalizes across image generation, video generation, and editing tasks. Experiments demonstrate a speedup of over 2.6x while maintaining high-quality outputs. The source code for this work can be found at https://github.com/Div290/FastFlow.

### 🤖 AI 总结

**一句话总结**：Flow-matching models deliver state-of-the-art fidelity in image and video generation, but the inherent sequential denoising process renders them slower. Existing acceleration methods like distillation...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：

**评分**：68

**论文链接**：[查看原文](https://arxiv.org/abs/2602.11105v1) | [下载PDF](https://arxiv.org/pdf/2602.11105v1.pdf)

---

## [14. First International StepUP Competition for Biometric Footstep Recognition: Methods, Results and Remaining Challenges](https://arxiv.org/abs/2602.11086v1)

**作者**：Robyn Larracy, Eve MacDonald, Angkoon Phinyomark 等 8 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-02-11

### 📄 论文摘要

Biometric footstep recognition, based on a person's unique pressure patterns under their feet during walking, is an emerging field with growing applications in security and safety. However, progress in this area has been limited by the lack of large, diverse datasets necessary to address critical challenges such as generalization to new users and robustness to shifts in factors like footwear or walking speed. The recent release of the UNB StepUP-P150 dataset, the largest and most comprehensive collection of high-resolution footstep pressure recordings to date, opens new opportunities for addressing these challenges through deep learning. To mark this milestone, the First International StepUP Competition for Biometric Footstep Recognition was launched. Competitors were tasked with developing robust recognition models using the StepUP-P150 dataset that were then evaluated on a separate, dedicated test set designed to assess verification performance under challenging variations, given limited and relatively homogeneous reference data. The competition attracted global participation, with 23 registered teams from academia and industry. The top-performing team, Saeid_UCC, achieved the best equal error rate (EER) of 10.77% using a generative reward machine (GRM) optimization strategy. Overall, the competition showcased strong solutions, but persistent challenges in generalizing to unfamiliar footwear highlight a critical area for future work.

### 🤖 AI 总结

**一句话总结**：Biometric footstep recognition, based on a person's unique pressure patterns under their feet during walking, is an emerging field with growing applications in security and safety. However, progress i...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.11086v1) | [下载PDF](https://arxiv.org/pdf/2602.11086v1.pdf)

---

## [15. Chatting with Images for Introspective Visual Thinking](https://arxiv.org/abs/2602.11073v1)

**作者**：Junfei Wu, Jian Guan, Qiang Liu 等 7 位作者  
**分类**：cs.CV, cs.AI, cs.CL  
**发布时间**：2026-02-11

### 📄 论文摘要

Current large vision-language models (LVLMs) typically rely on text-only reasoning based on a single-pass visual encoding, which often leads to loss of fine-grained visual information. Recently the proposal of ''thinking with images'' attempts to alleviate this limitation by manipulating images via external tools or code; however, the resulting visual states are often insufficiently grounded in linguistic semantics, impairing effective cross-modal alignment - particularly when visual semantics or geometric relationships must be reasoned over across distant regions or multiple images. To address these challenges, we propose ''chatting with images'', a new framework that reframes visual manipulation as language-guided feature modulation. Under the guidance of expressive language prompts, the model dynamically performs joint re-encoding over multiple image regions, enabling tighter coupling between linguistic reasoning and visual state updates. We instantiate this paradigm in ViLaVT, a novel LVLM equipped with a dynamic vision encoder explicitly designed for such interactive visual reasoning, and trained it with a two-stage curriculum combining supervised fine-tuning and reinforcement learning to promote effective reasoning behaviors. Extensive experiments across eight benchmarks demonstrate that ViLaVT achieves strong and consistent improvements, with particularly pronounced gains on complex multi-image and video-based spatial reasoning tasks.

### 🤖 AI 总结

**一句话总结**：Current large vision-language models (LVLMs) typically rely on text-only reasoning based on a single-pass visual encoding, which often leads to loss of fine-grained visual information. Recently the pr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.11073v1) | [下载PDF](https://arxiv.org/pdf/2602.11073v1.pdf)

---

## [16. PuriLight: A Lightweight Shuffle and Purification Framework for Monocular Depth Estimation](https://arxiv.org/abs/2602.11066v1)

**作者**：Yujie Chen, Li Zhang, Xiaomeng Chu 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-11

### 📄 论文摘要

We propose PuriLight, a lightweight and efficient framework for self-supervised monocular depth estimation, to address the dual challenges of computational efficiency and detail preservation. While recent advances in self-supervised depth estimation have reduced reliance on ground truth supervision, existing approaches remain constrained by either bulky architectures compromising practicality or lightweight models sacrificing structural precision. These dual limitations underscore the critical need to develop lightweight yet structurally precise architectures. Our framework addresses these limitations through a three-stage architecture incorporating three novel modules: the Shuffle-Dilation Convolution (SDC) module for local feature extraction, the Rotation-Adaptive Kernel Attention (RAKA) module for hierarchical feature enhancement, and the Deep Frequency Signal Purification (DFSP) module for global feature purification. Through effective collaboration, these modules enable PuriLight to achieve both lightweight and accurate feature extraction and processing. Extensive experiments demonstrate that PuriLight achieves state-of-the-art performance with minimal training parameters while maintaining exceptional computational efficiency. Codes will be available at https://github.com/ishrouder/PuriLight.

### 🤖 AI 总结

**一句话总结**：We propose PuriLight, a lightweight and efficient framework for self-supervised monocular depth estimation, to address the dual challenges of computational efficiency and detail preservation. While re...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：

**评分**：60

**论文链接**：[查看原文](https://arxiv.org/abs/2602.11066v1) | [下载PDF](https://arxiv.org/pdf/2602.11066v1.pdf)

---

## cs.LG

## [17. Diffusion-Pretrained Dense and Contextual Embeddings](https://arxiv.org/abs/2602.11151v1)

**作者**：Sedigheh Eslami, Maksim Gaiduk, Markus Krimmel 等 6 位作者  
**分类**：cs.LG, cs.CL, cs.IR  
**发布时间**：2026-02-11

### 📄 论文摘要

In this report, we introduce pplx-embed, a family of multilingual embedding models that employ multi-stage contrastive learning on a diffusion-pretrained language model backbone for web-scale retrieval. By leveraging bidirectional attention through diffusion-based pretraining, our models capture comprehensive bidirectional context within passages, enabling the use of mean pooling and a late chunking strategy to better preserve global context across long documents. We release two model types: pplx-embed-v1 for standard retrieval, and pplx-embed-context-v1 for contextualized embeddings that incorporate global document context into passage representations. pplx-embed-v1 achieves competitive performance on the MTEB(Multilingual, v2), MTEB(Code), MIRACL, BERGEN, and ToolRet retrieval benchmarks, while pplx-embed-context-v1 sets new records on the ConTEB benchmark. Beyond public benchmarks, pplx-embed-v1 demonstrates strong performance on our internal evaluation suite, which focuses on real-world, large-scale search scenarios over tens of millions of documents. These results validate the models' effectiveness in production environments where retrieval quality and efficiency are critical at scale.

### 🤖 AI 总结

**一句话总结**：In this report, we introduce pplx-embed, a family of multilingual embedding models that employ multi-stage contrastive learning on a diffusion-pretrained language model backbone for web-scale retrieva...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2602.11151v1) | [下载PDF](https://arxiv.org/pdf/2602.11151v1.pdf)

---

## [18. GENIUS: Generative Fluid Intelligence Evaluation Suite](https://arxiv.org/abs/2602.11144v1)

**作者**：Ruichuan An, Sihan Yang, Ziyu Guo 等 11 位作者  
**分类**：cs.LG, cs.AI, cs.CV  
**发布时间**：2026-02-11

### 📄 论文摘要

Unified Multimodal Models (UMMs) have shown remarkable progress in visual generation. Yet, existing benchmarks predominantly assess $\textit{Crystallized Intelligence}$, which relies on recalling accumulated knowledge and learned schemas. This focus overlooks $\textit{Generative Fluid Intelligence (GFI)}$: the capacity to induce patterns, reason through constraints, and adapt to novel scenarios on the fly. To rigorously assess this capability, we introduce $\textbf{GENIUS}$ ($\textbf{GEN}$ Fluid $\textbf{I}$ntelligence Eval$\textbf{U}$ation $\textbf{S}$uite). We formalize $\textit{GFI}$ as a synthesis of three primitives. These include $\textit{Inducing Implicit Patterns}$ (e.g., inferring personalized visual preferences), $\textit{Executing Ad-hoc Constraints}$ (e.g., visualizing abstract metaphors), and $\textit{Adapting to Contextual Knowledge}$ (e.g., simulating counter-intuitive physics). Collectively, these primitives challenge models to solve problems grounded entirely in the immediate context. Our systematic evaluation of 12 representative models reveals significant performance deficits in these tasks. Crucially, our diagnostic analysis disentangles these failure modes. It demonstrates that deficits stem from limited context comprehension rather than insufficient intrinsic generative capability. To bridge this gap, we propose a training-free attention intervention strategy. Ultimately, $\textbf{GENIUS}$ establishes a rigorous standard for $\textit{GFI}$, guiding the field beyond knowledge utilization toward dynamic, general-purpose reasoning. Our dataset and code will be released at: $\href{https://github.com/arctanxarc/GENIUS}{https://github.com/arctanxarc/GENIUS}$.

### 🤖 AI 总结

**一句话总结**：Unified Multimodal Models (UMMs) have shown remarkable progress in visual generation. Yet, existing benchmarks predominantly assess $\textit{Crystallized Intelligence}$, which relies on recalling accu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：

**评分**：64

**论文链接**：[查看原文](https://arxiv.org/abs/2602.11144v1) | [下载PDF](https://arxiv.org/pdf/2602.11144v1.pdf)

---

## [19. TabICLv2: A better, faster, scalable, and open tabular foundation model](https://arxiv.org/abs/2602.11139v1)

**作者**：Jingang Qu, David Holzmüller, Gaël Varoquaux 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-11

### 📄 论文摘要

Tabular foundation models, such as TabPFNv2 and TabICL, have recently dethroned gradient-boosted trees at the top of predictive benchmarks, demonstrating the value of in-context learning for tabular data. We introduce TabICLv2, a new state-of-the-art foundation model for regression and classification built on three pillars: (1) a novel synthetic data generation engine designed for high pretraining diversity; (2) various architectural innovations, including a new scalable softmax in attention improving generalization to larger datasets without prohibitive long-sequence pretraining; and (3) optimized pretraining protocols, notably replacing AdamW with the Muon optimizer. On the TabArena and TALENT benchmarks, TabICLv2 without any tuning surpasses the performance of the current state of the art, RealTabPFN-2.5 (hyperparameter-tuned, ensembled, and fine-tuned on real data). With only moderate pretraining compute, TabICLv2 generalizes effectively to million-scale datasets under 50GB GPU memory while being markedly faster than RealTabPFN-2.5. We provide extensive ablation studies to quantify these contributions and commit to open research by first releasing inference code and model weights at https://github.com/soda-inria/tabicl, with synthetic data engine and pretraining code to follow.

### 🤖 AI 总结

**一句话总结**：Tabular foundation models, such as TabPFNv2 and TabICL, have recently dethroned gradient-boosted trees at the top of predictive benchmarks, demonstrating the value of in-context learning for tabular d...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2602.11139v1) | [下载PDF](https://arxiv.org/pdf/2602.11139v1.pdf)

---

## [20. Weight Decay Improves Language Model Plasticity](https://arxiv.org/abs/2602.11137v1)

**作者**：Tessa Han, Sebastian Bordt, Hanlin Zhang 等 4 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-02-11

### 📄 论文摘要

The prevailing paradigm in large language model (LLM) development is to pretrain a base model, then perform further training to improve performance and model behavior. However, hyperparameter optimization and scaling laws have been studied primarily from the perspective of the base model's validation loss, ignoring downstream adaptability. In this work, we study pretraining from the perspective of model plasticity, that is, the ability of the base model to successfully adapt to downstream tasks through fine-tuning. We focus on the role of weight decay, a key regularization parameter during pretraining. Through systematic experiments, we show that models trained with larger weight decay values are more plastic, meaning they show larger performance gains when fine-tuned on downstream tasks. This phenomenon can lead to counterintuitive trade-offs where base models that perform worse after pretraining can perform better after fine-tuning. Further investigation of weight decay's mechanistic effects on model behavior reveals that it encourages linearly separable representations, regularizes attention matrices, and reduces overfitting on the training data. In conclusion, this work demonstrates the importance of using evaluation metrics beyond cross-entropy loss for hyperparameter optimization and casts light on the multifaceted role of that a single optimization hyperparameter plays in shaping model behavior.

### 🤖 AI 总结

**一句话总结**：The prevailing paradigm in large language model (LLM) development is to pretrain a base model, then perform further training to improve performance and model behavior. However, hyperparameter optimiza...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2602.11137v1) | [下载PDF](https://arxiv.org/pdf/2602.11137v1.pdf)

---

## [21. From Circuits to Dynamics: Understanding and Stabilizing Failure in 3D Diffusion Transformers](https://arxiv.org/abs/2602.11130v1)

**作者**：Maximilian Plattner, Fabian Paischer, Johannes Brandstetter 等 4 位作者  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-02-11

### 📄 论文摘要

Reliable surface completion from sparse point clouds underpins many applications spanning content creation and robotics. While 3D diffusion transformers attain state-of-the-art results on this task, we uncover that they exhibit a catastrophic mode of failure: arbitrarily small on-surface perturbations to the input point cloud can fracture the output into multiple disconnected pieces -- a phenomenon we call Meltdown. Using activation-patching from mechanistic interpretability, we localize Meltdown to a single early denoising cross-attention activation. We find that the singular-value spectrum of this activation provides a scalar proxy: its spectral entropy rises when fragmentation occurs and returns to baseline when patched. Interpreted through diffusion dynamics, we show that this proxy tracks a symmetry-breaking bifurcation of the reverse process. Guided by this insight, we introduce PowerRemap, a test-time control that stabilizes sparse point-cloud conditioning. We demonstrate that Meltdown persists across state-of-the-art architectures (WaLa, Make-a-Shape), datasets (GSO, SimJEB) and denoising strategies (DDPM, DDIM), and that PowerRemap effectively counters this failure with stabilization rates of up to 98.3%. Overall, this work is a case study on how diffusion model behavior can be understood and guided based on mechanistic analysis, linking a circuit-level cross-attention mechanism to diffusion-dynamics accounts of trajectory bifurcations.

### 🤖 AI 总结

**一句话总结**：Reliable surface completion from sparse point clouds underpins many applications spanning content creation and robotics. While 3D diffusion transformers attain state-of-the-art results on this task, w...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2602.11130v1) | [下载PDF](https://arxiv.org/pdf/2602.11130v1.pdf)

---

## [22. Asymmetric Prompt Weighting for Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2602.11128v1)

**作者**：Reinhard Heckel, Mahdi Soltanolkotabi, Christos Thramboulidis  
**分类**：cs.LG  
**发布时间**：2026-02-11

### 📄 论文摘要

Reinforcement learning with verifiable rewards has driven recent advances in LLM post-training, in particular for reasoning. Policy optimization algorithms generate a number of responses for a given prompt and then effectively weight the corresponding gradients depending on the rewards. The most popular algorithms including GRPO, DAPO, and RLOO focus on ambiguous prompts, i.e., prompts with intermediate success probability, while downgrading gradients with very easy and very hard prompts. In this paper, we consider asymmetric prompt weightings that assign higher weights to prompts with low, or even zero, empirical success probability. We find that asymmetric weighting particularly benefits from-scratch RL (as in R1-Zero), where training traverses a wide accuracy range, and less so in post-SFT RL where the model already starts at high accuracy. We also provide theory that characterizes prompt weights which minimize the time needed to raise success probability from an initial level to a target accuracy under a fixed update budget. In low-success regimes, where informative responses are rare and response cost dominates, these optimal weights become asymmetric, upweighting low success probabilities and thereby accelerating effective-time convergence.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning with verifiable rewards has driven recent advances in LLM post-training, in particular for reasoning. Policy optimization algorithms generate a number of responses for a given p...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：

**评分**：67

**论文链接**：[查看原文](https://arxiv.org/abs/2602.11128v1) | [下载PDF](https://arxiv.org/pdf/2602.11128v1.pdf)

---

## [23. The Offline-Frontier Shift: Diagnosing Distributional Limits in Generative Multi-Objective Optimization](https://arxiv.org/abs/2602.11126v1)

**作者**：Stephanie Holly, Alexandru-Ciprian Zăvoianu, Siegfried Silber 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-11

### 📄 论文摘要

Offline multi-objective optimization (MOO) aims to recover Pareto-optimal designs given a finite, static dataset. Recent generative approaches, including diffusion models, show strong performance under hypervolume, yet their behavior under other established MOO metrics is less understood. We show that generative methods systematically underperform evolutionary alternatives with respect to other metrics, such as generational distance. We relate this failure mode to the offline-frontier shift, i.e., the displacement of the offline dataset from the Pareto front, which acts as a fundamental limitation in offline MOO. We argue that overcoming this limitation requires out-of-distribution sampling in objective space (via an integral probability metric) and empirically observe that generative methods remain conservatively close to the offline objective distribution. Our results position offline MOO as a distribution-shift--limited problem and provide a diagnostic lens for understanding when and why generative optimization methods fail.

### 🤖 AI 总结

**一句话总结**：Offline multi-objective optimization (MOO) aims to recover Pareto-optimal designs given a finite, static dataset. Recent generative approaches, including diffusion models, show strong performance unde...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：

**评分**：56

**论文链接**：[查看原文](https://arxiv.org/abs/2602.11126v1) | [下载PDF](https://arxiv.org/pdf/2602.11126v1.pdf)

---

## [24. From Natural Language to Materials Discovery:The Materials Knowledge Navigation Agent](https://arxiv.org/abs/2602.11123v1)

**作者**：Genmao Zhuang, Amir Barati Farimani  
**分类**：cs.LG, cond-mat.mtrl-sci  
**发布时间**：2026-02-11

### 📄 论文摘要

Accelerating the discovery of high-performance materials remains a central challenge across energy, electronics, and aerospace technologies, where traditional workflows depend heavily on expert intuition and computationally expensive simulations. Here we introduce the Materials Knowledge Navigation Agent (MKNA), a language-driven system that translates natural-language scientific intent into executable actions for database retrieval, property prediction, structure generation, and stability evaluation. Beyond automating tool invocation, MKNA autonomously extracts quantitative thresholds and chemically meaningful design motifs from literature and database evidence, enabling data-grounded hypothesis formation. Applied to the search for high-Debye-temperature ceramics, the agent identifies a literature-supported screening criterion (Theta_D > 800 K), rediscovers canonical ultra-stiff materials such as diamond, SiC, SiN, and BeO, and proposes thermodynamically stable, previously unreported Be-C-rich compounds that populate the sparsely explored 1500-1700 K regime. These results demonstrate that MKNA not only finds stable candidates but also reconstructs interpretable design heuristics, establishing a generalizable platform for autonomous, language-guided materials exploration.

### 🤖 AI 总结

**一句话总结**：Accelerating the discovery of high-performance materials remains a central challenge across energy, electronics, and aerospace technologies, where traditional workflows depend heavily on expert intuit...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2602.11123v1) | [下载PDF](https://arxiv.org/pdf/2602.11123v1.pdf)

---

## [25. MerLin: A Discovery Engine for Photonic and Hybrid Quantum Machine Learning](https://arxiv.org/abs/2602.11092v1)

**作者**：Cassandre Notton, Benjamin Stott, Philippe Schoeb 等 10 位作者  
**分类**：cs.LG, cs.PL, quant-ph  
**发布时间**：2026-02-11

### 📄 论文摘要

Identifying where quantum models may offer practical benefits in near term quantum machine learning (QML) requires moving beyond isolated algorithmic proposals toward systematic and empirical exploration across models, datasets, and hardware constraints. We introduce MerLin, an open source framework designed as a discovery engine for photonic and hybrid quantum machine learning. MerLin integrates optimized strong simulation of linear optical circuits into standard PyTorch and scikit learn workflows, enabling end to end differentiable training of quantum layers. MerLin is designed around systematic benchmarking and reproducibility. As an initial contribution, we reproduce eighteen state of the art photonic and hybrid QML works spanning kernel methods, reservoir computing, convolutional and recurrent architectures, generative models, and modern training paradigms. These reproductions are released as reusable, modular experiments that can be directly extended and adapted, establishing a shared experimental baseline consistent with empirical benchmarking methodologies widely adopted in modern artificial intelligence. By embedding photonic quantum models within established machine learning ecosystems, MerLin allows practitioners to leverage existing tooling for ablation studies, cross modality comparisons, and hybrid classical quantum workflows. The framework already implements hardware aware features, allowing tests on available quantum hardware while enabling exploration beyond its current capabilities, positioning MerLin as a future proof co design tool linking algorithms, benchmarks, and hardware.

### 🤖 AI 总结

**一句话总结**：Identifying where quantum models may offer practical benefits in near term quantum machine learning (QML) requires moving beyond isolated algorithmic proposals toward systematic and empirical explorat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2602.11092v1) | [下载PDF](https://arxiv.org/pdf/2602.11092v1.pdf)

---

## [26. General Flexible $f$-divergence for Challenging Offline RL Datasets with Low Stochasticity and Diverse Behavior Policies](https://arxiv.org/abs/2602.11087v1)

**作者**：Jianxun Wang, Grant C. Forbes, Leonardo Villalobos-Arias 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-11

### 📄 论文摘要

Offline RL algorithms aim to improve upon the behavior policy that produces the collected data while constraining the learned policy to be within the support of the dataset. However, practical offline datasets often contain examples with little diversity or limited exploration of the environment, and from multiple behavior policies with diverse expertise levels. Limited exploration can impair the offline RL algorithm's ability to estimate \textit{Q} or \textit{V} values, while constraining towards diverse behavior policies can be overly conservative. Such datasets call for a balance between the RL objective and behavior policy constraints. We first identify the connection between $f$-divergence and optimization constraint on the Bellman residual through a more general Linear Programming form for RL and the convex conjugate. Following this, we introduce the general flexible function formulation for the $f$-divergence to incorporate an adaptive constraint on algorithms' learning objectives based on the offline training dataset. Results from experiments on the MuJoCo, Fetch, and AdroitHand environments show the correctness of the proposed LP form and the potential of the flexible $f$-divergence in improving performance for learning from a challenging dataset when applied to a compatible constrained optimization algorithm.

### 🤖 AI 总结

**一句话总结**：Offline RL algorithms aim to improve upon the behavior policy that produces the collected data while constraining the learned policy to be within the support of the dataset. However, practical offline...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：

**评分**：55

**论文链接**：[查看原文](https://arxiv.org/abs/2602.11087v1) | [下载PDF](https://arxiv.org/pdf/2602.11087v1.pdf)

---

## [27. GRASP: group-Shapley feature selection for patients](https://arxiv.org/abs/2602.11084v1)

**作者**：Yuheng Luo, Shuyan Li, Zhong Cao  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-11

### 📄 论文摘要

Feature selection remains a major challenge in medical prediction, where existing approaches such as LASSO often lack robustness and interpretability. We introduce GRASP, a novel framework that couples Shapley value driven attribution with group $L_{21}$ regularization to extract compact and non-redundant feature sets. GRASP first distills group level importance scores from a pretrained tree model via SHAP, then enforces structured sparsity through group $L_{21}$ regularized logistic regression, yielding stable and interpretable selections. Extensive comparisons with LASSO, SHAP, and deep learning based methods show that GRASP consistently delivers comparable or superior predictive accuracy, while identifying fewer, less redundant, and more stable features.

### 🤖 AI 总结

**一句话总结**：Feature selection remains a major challenge in medical prediction, where existing approaches such as LASSO often lack robustness and interpretability. We introduce GRASP, a novel framework that couple...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：

**评分**：64

**论文链接**：[查看原文](https://arxiv.org/abs/2602.11084v1) | [下载PDF](https://arxiv.org/pdf/2602.11084v1.pdf)

---

## [28. In-the-Wild Model Organisms: Mitigating Undesirable Emergent Behaviors in Production LLM Post-Training via Data Attribution](https://arxiv.org/abs/2602.11079v1)

**作者**：Frank Xiao, Santiago Aranguri  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-11

### 📄 论文摘要

We propose activation-based data attribution, a method that traces behavioral changes in post-trained language models to responsible training datapoints. By computing activation-difference vectors for both test prompts and preference pairs and ranking by cosine similarity, we identify datapoints that cause specific behaviors and validate these attributions causally by retraining with modified data. Clustering behavior-datapoint similarity matrices also enables unsupervised discovery of emergent behaviors. Applying this to OLMo 2's production DPO training, we surfaced distractor-triggered compliance: a harmful behavior where the model complies with dangerous requests when benign formatting instructions are appended. Filtering top-ranked datapoints reduces this behavior by 63% while switching their labels achieves 78%. Our method outperforms gradient-based attribution and LLM-judge baselines while being over 10 times cheaper than both. This in-the-wild model organism - emerging from contaminated preference data rather than deliberate injection - provides a realistic benchmark for safety techniques.

### 🤖 AI 总结

**一句话总结**：We propose activation-based data attribution, a method that traces behavioral changes in post-trained language models to responsible training datapoints. By computing activation-difference vectors for...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：

**评分**：68

**论文链接**：[查看原文](https://arxiv.org/abs/2602.11079v1) | [下载PDF](https://arxiv.org/pdf/2602.11079v1.pdf)

---

## [29. Motion Capture is Not the Target Domain: Scaling Synthetic Data for Learning Motion Representations](https://arxiv.org/abs/2602.11064v1)

**作者**：Firas Darwish, George Nicholson, Aiden Doherty 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-11

### 📄 论文摘要

Synthetic data offers a compelling path to scalable pretraining when real-world data is scarce, but models pretrained on synthetic data often fail to transfer reliably to deployment settings. We study this problem in full-body human motion, where large-scale data collection is infeasible but essential for wearable-based Human Activity Recognition (HAR), and where synthetic motion can be generated from motion-capture-derived representations. We pretrain motion time-series models using such synthetic data and evaluate their transfer across diverse downstream HAR tasks. Our results show that synthetic pretraining improves generalisation when mixed with real data or scaled sufficiently. We also demonstrate that large-scale motion-capture pretraining yields only marginal gains due to domain mismatch with wearable signals, clarifying key sim-to-real challenges and the limits and opportunities of synthetic motion data for transferable HAR representations.

### 🤖 AI 总结

**一句话总结**：Synthetic data offers a compelling path to scalable pretraining when real-world data is scarce, but models pretrained on synthetic data often fail to transfer reliably to deployment settings. We study...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：

**评分**：65

**论文链接**：[查看原文](https://arxiv.org/abs/2602.11064v1) | [下载PDF](https://arxiv.org/pdf/2602.11064v1.pdf)

---

## [30. Divide, Harmonize, Then Conquer It: Shooting Multi-Commodity Flow Problems with Multimodal Language Models](https://arxiv.org/abs/2602.11057v1)

**作者**：Xinyu Yuan, Yan Qiao, Zonghui Wang 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-11

### 📄 论文摘要

The multi-commodity flow (MCF) problem is a fundamental topic in network flow and combinatorial optimization, with broad applications in transportation, communication, and logistics, etc. Nowadays, the rapid expansion of allocation systems has posed challenges for existing optimization engines in balancing optimality and tractability. In this paper, we present Pram, the first ML-based method that leverages the reasoning power of multimodal language models (MLMs) for addressing the trade-off dilemma -- a great need of service providers. As part of our proposal, Pram (i) quickly computes high-quality allocations by dividing the original problem into local subproblems, which are then resolved by an MLM-powered "agent", and (ii) ensures global consistency by harmonizing these subproblems via a multi-agent reinforcement learning algorithm. Theoretically, we show that Pram, which learns to perform gradient descent in context, provably converges to the optimum within the family of MCF problems. Empirically, on real-world datasets and public topologies, Pram achieves performance comparable to, and in some cases even surpassing, linear programming solvers (very close to the optimal solution), and substantially lower runtimes (1 to 2 orders of magnitude faster). Moreover, Pram exhibits strong robustness (<10\% performance degradation under link failures or flow bursts), demonstrating MLM's generalization ability to unforeseen events. Pram is objective-agnostic and seamlessly integrates with mainstream allocation systems, providing a practical and scalable solution for future networks.

### 🤖 AI 总结

**一句话总结**：The multi-commodity flow (MCF) problem is a fundamental topic in network flow and combinatorial optimization, with broad applications in transportation, communication, and logistics, etc. Nowadays, th...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2602.11057v1) | [下载PDF](https://arxiv.org/pdf/2602.11057v1.pdf)

---

