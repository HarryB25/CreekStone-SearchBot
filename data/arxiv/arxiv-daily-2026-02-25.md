# arXiv AI 论文日报 | 2026-02-25

> 共 2 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (2 篇)

---

## cs.CV

## [1. Neu-PiG: Neural Preconditioned Grids for Fast Dynamic Surface Reconstruction on Long Sequences](https://arxiv.org/abs/2602.22212v1)

**作者**：Julian Kaltheuner, Hannah Dröge, Markus Plack 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-25

### 📄 论文摘要

Temporally consistent surface reconstruction of dynamic 3D objects from unstructured point cloud data remains challenging, especially for very long sequences. Existing methods either optimize deformations incrementally, risking drift and requiring long runtimes, or rely on complex learned models that demand category-specific training. We present Neu-PiG, a fast deformation optimization method based on a novel preconditioned latent-grid encoding that distributes spatial features parameterized on the position and normal direction of a keyframe surface. Our method encodes entire deformations across all time steps at various spatial scales into a multi-resolution latent grid, parameterized by the position and normal direction of a reference surface from a single keyframe. This latent representation is then augmented for time modulation and decoded into per-frame 6-DoF deformations via a lightweight multilayer perceptron (MLP). To achieve high-fidelity, drift-free surface reconstructions in seconds, we employ Sobolev preconditioning during gradient-based training of the latent space, completely avoiding the need for any explicit correspondences or further priors. Experiments across diverse human and animal datasets demonstrate that Neu-PiG outperforms state-the-art approaches, offering both superior accuracy and scalability to long sequences while running at least 60x faster than existing training-free methods and achieving inference speeds on the same order as heavy pretrained models.

### 🤖 AI 总结

**一句话总结**：Neu-PiG 通过“法线条件化”的多分辨率潜变量网格编码与 Sobolev 预条件优化，实现长序列动态物体的快速、无漂移高质量表面重建。

**研究动机**：长序列动态点云的时序一致重建难点在于：增量形变优化易漂移且耗时，而依赖学习模型的方法常需类别特定训练、结构复杂。作者希望在无需显式对应与强先验的前提下，实现秒级、可扩展的高保真重建。

**核心方法**：以单帧关键帧表面为参考，将空间特征按“位置+法线方向”参数化并编码进跨尺度多分辨率潜变量网格，结合时间调制后由轻量 MLP 解码为每帧 6-DoF 形变。训练时在潜空间使用 Sobolev 预条件的梯度优化以加速收敛并抑制漂移，全程不依赖显式对应关系。

**主要结论**：在多类人/动物数据上，Neu-PiG 在精度与长序列可扩展性上优于现有方法，同时相较训练-free 方法至少快 60×，并达到接近重型预训练模型的推理速度。整体证明了预条件化潜网格表示可在不引入复杂学习先验的情况下实现快速且稳定的动态重建。

**关键词**：动态表面重建, 时序一致性重建, 长序列三维重建, 无结构点云, 形变优化, 多分辨率隐式网格编码, 潜空间预条件化, 关键帧参考表面, 无对应关系重建, 6-DoF形变, 轻量级MLP解码器

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2602.22212v1) | [下载PDF](https://arxiv.org/pdf/2602.22212v1.pdf)

---

## [2. WHOLE: World-Grounded Hand-Object Lifted from Egocentric Videos](https://arxiv.org/abs/2602.22209v1)

**作者**：Yufei Ye, Jiaman Li, Ryan Rong 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-25

### 📄 论文摘要

Egocentric manipulation videos are highly challenging due to severe occlusions during interactions and frequent object entries and exits from the camera view as the person moves. Current methods typically focus on recovering either hand or object pose in isolation, but both struggle during interactions and fail to handle out-of-sight cases. Moreover, their independent predictions often lead to inconsistent hand-object relations. We introduce WHOLE, a method that holistically reconstructs hand and object motion in world space from egocentric videos given object templates. Our key insight is to learn a generative prior over hand-object motion to jointly reason about their interactions. At test time, the pretrained prior is guided to generate trajectories that conform to the video observations. This joint generative reconstruction substantially outperforms approaches that process hands and objects separately followed by post-processing. WHOLE achieves state-of-the-art performance on hand motion estimation, 6D object pose estimation, and their relative interaction reconstruction. Project website: https://judyye.github.io/whole-www

### 🤖 AI 总结

**一句话总结**：WHOLE通过学习手-物交互的生成式先验，在第一视角视频中联合重建手与物体在世界坐标系下的运动轨迹，并显著提升交互一致性与遮挡/出视野鲁棒性。

**研究动机**：第一视角操作视频中手与物体强遮挡且物体频繁出入视野，分别估计手或物体姿态的方法在交互与缺失观测时容易失败。独立预测还会导致手-物关系不一致，难以可靠重建真实交互过程。

**核心方法**：方法学习一个生成式的手-物运动先验（联合建模交互轨迹），并在测试时用视频观测对该先验进行引导/约束，使生成的手与物体轨迹同时匹配图像证据与物理交互关系。输入包含物体模板，从而在世界空间中同步恢复手运动与物体6D位姿及相对关系。

**主要结论**：联合生成式重建相比“手/物分别估计+后处理”在遮挡与出视野场景更稳健，显著提升手运动、物体6D位姿以及手-物相对交互重建质量。WHOLE在相关基准上达到或刷新SOTA表现。

**关键词**：WHOLE, World-Grounded, Hand-Object, Lifted, Egocentric, Videos, manipulation, highly

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2602.22209v1) | [下载PDF](https://arxiv.org/pdf/2602.22209v1.pdf)

---

