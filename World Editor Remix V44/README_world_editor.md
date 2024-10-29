# 地图编辑器
    https://metin2.dev/topic/2747-worldeditor-remix/

### 安装
https://metin2.dev/topic/21827-installing-the-world-editor-remix/#comment-118622
https://metin2.dev/topic/25611-how-can-i-install-world-editor-v38/#comment-135874
- 1：下载 WorldEditor ReMIX：
- 2：在 D:\ Drive 上创建一个名为“ymir work”的文件夹并将下载文件放在那里。
- 3：从客户端复制“ymir work”文件夹中的以下文件：
  Devil.dll
  ilu.dll
  mss32.dll
  SpeedTreeRT.dll
- 4：从您的客户端解压以下文件并将其放入“ymir work”文件夹中：
  effect
  environment (You can find this folder in "etc").
  special (You can find this folder in "etc").
  property
  terrainmaps (You can find this folder in "terrain").
  textureset
  tree
  zone
  正确路径如下：D:\ymir work\zone\a
- 4.1：如果您解压文件，请确保您进入了正确的文件夹！
  例如：
  pack\effect\ymir work\ effect
- 5：如果您想在 WorldEditor 中看到您的角色，请添加以下内容。
  -创建以下文件夹：ymir work\pc\sura

  在 sura 文件夹中添加来自客户端的以下内容：
  sura_face.dds
  sura_novice.gr2
  sura_novice_black.dds

  在 sura 文件夹中创建以下文件夹：  onehand_sword并从您的客户端复制您可以在onehand_sword 文件夹中找到的
  “ wait.gr2 ” 。
- 把地图文件复制D:\ymir work，然后选择load对象预览
- 要渲染/刷新所有对象 + 阴影：
  首先按“T”键以确保您的相机与捕捉整个世界的角度对齐。然后按“F6”键重新渲染小地图和阴影

### 配置信息

；信息：
;-) 100% 已翻译
;-) 奶奶2.11
;-) F6 作为插入替代
; -) worldeditor_en 中不存在许多默认功能（可能该二进制文件很久以前从 SVN 中取出并被黑客入侵），例如所有区域和天空盒的 Ins
; -) WASD UPLEFTDOWNRIGHT 移动（+异步对角线移动）
; -) 上-左-下-右移动*10（+异步对角线移动）
;-) 配置文件用于一些事情
；默认输出选项
; 其他一些功能，例如默认的 WASD 移动
; Insert 是否应该让你回到你之前所在的位置
；保存地图集时没有 MAI 转储
；DevIL 是否应该压缩并从 minimap.dds 中删除 alpha
;是否加载.mdatr建筑高度
；创建地图时的默认纹理集
; 重叠标签
；其他东西
;-) 修复了几个错误
; 默认标题应用名称
; 尝试在创建新地图时写入一个空的纹理集名称
；每次加载时 ViewRadius 都会加倍&save
; shadowmap.dds 创建
; 保存图集时断言
；调整高度时崩溃
；许多缓冲区溢出
；*.mdc 碰撞数据保存（用于 game_test）
；加载地图时不检查输出选项
；水刷水 ID 错误（每次调用该函数时，ID 都会增加到 256；现在它基于水高，就像它应该的那样）
；初始化纹理贴图重新加载贴图崩溃并且最后 2px 总是空白
; 方形，适合上下高度的刷子
；添加纹理集纹理按钮（+多选）
; 删除纹理集纹理特征（只需从列表中选择一个纹理并按 DELETE 键）
；创建索引为 -1（更改为 0）的空纹理集
；改变基本位置按钮
；拼写错误
；天空盒底部图像（注：您还需要一个固定的启动器）
; 删除了编辑日光/属性时无聊的 CTRL 要求（移动相机）
; 修复按下向下/向上键（就像单击它们时一样）时刷新纹理图像框的问题
; 修复了如果不存在则创建 TextureSet 文件的问题
; 修复了新的狼人动作事件处理
; 修复编辑动画攻击骨骼时发生崩溃且 00010.gr2 丢失的问题
; 修复 locale/ymir/mob_proto 加载（它自动检测最常见的结构）和 <map>/regen.txt 加载/保存
; 修复 ./group.txt 加载
; 修复了加载/保存/编辑 <map>/regen.txt 的问题（对于“m”再生来说非常好，对于“g”还未测试）
；如果 pack/property 存在，则可从 PACK 加载！请确保 pack/Index 存在！
; 修复多对象选择崩溃问题
; 修复预览缺失纹理时崩溃的问题
; 修复切换地图时不清除旧环境（例如天空盒）的问题
; 修复了在根树（对象选项卡）中不创建属性文件夹的问题
; 修复模型选项卡中的对象附件
; 修复了“效果”选项卡中新粒子的名称
; 修复了保存没有网格模型的 .mse 脚本时崩溃的问题
; 修复插入较低梯度时崩溃的问题
;-) 在创建新地图时创建了新的 TextureSet 字段
;-) 双击纹理时创建新的“更改/删除纹理”按钮
;-) 创建了背景音乐播放和阴影重新计算按钮
;-) 创建了水位高度“设置 0z”、“+1z”、“-1z”按钮
;-) server_attr 生成器
; -) 每次崩溃都会生成一个 logs/WorldEditorRemix_{target}_{date}.dmp 文件，可用于调试
;-) 实现了“水路”地图设置选项（启动器需要额外的代码）
;-) 实现了“风力”msenv 选项（启动器需要额外的代码）
;-)“加密数据”功能不起作用（未实现）
; 笔记：
；0) 此版本中没有回归！此处的错误意味着它也会存在于旧 WE 版本中！
; 1) 阴影输出选项比较棘手：调用 UpdateUI 时，尽管已按下检查，但阴影仍会被隐藏（我为此实现了阴影重新计算功能）# 自 v11 起已修复
; 2) 背景音乐播放器需要 /miles，并且淡入/淡出功能只有在您加载地图后才起作用
; 3) 仅当检测到 mdatr 高度时，调整高度按钮才有效
; 4) 调试版本在处理 n_flame_dungeon 和 n_ice_dungeon 等地图时会滞后（默认情况下，因为 SphereRadius 在 SphereLib\spherepack.h 中进行了密集检查）
; 5) 如果您加载地图，脚本面板（您加载 .msa 等文件的地方）的相机视角将会有点混乱（0z 而不是 -32767z 或 0x 0y -163,94z）
；6）一些树木物体放置在地面上后不可移动和/或突出显示，并且它们的选择是不可见的（你仍然可以删除它们）
；技巧：画一个正方形，选择一个普通建筑物并将它们选中，然后移动该建筑物，你会看到它们全部都会被移动！
; 7) server_attr 生成器将清除所有未使用的标志！attr[idx]&=~0xFFFFFFF8;
; 8) 您可以从 pack/Index 'n stuff 读取文件，但请注意，属性将不被考虑！#fixed since v15
；9）MonsterAreaInfo 功能非常滞后且漏洞百出
; 10) 尽管您可以一次选择多个纹理（使用 ctrl + 单击纹理集列表；进行刷涂或初始化基础纹理），但您不能同时删除多个纹理
; 11) .mdatr 高度比较棘手；如果你移动一栋建筑，高度将不会刷新，直到你放置一栋新建筑或任何你想要触发更新事件的东西
; 12) 默认情况下，世界编辑器尝试仅渲染 32x32px 区域的前 8 个地形纹理（注：1x1 地图是 256x256 px 区域）
；13) 由于 ymir 缓存故障，小地图渲染无法捕捉到前 2x2 区域内的建筑物/树木，您需要设置相机才能“看到”它们
; 14) 当纹理集、环境等加载失败时，旧文件名仍然保持加载
；15) 属性标志“3”（三）没有实现，所以不要使用它！
；16) 从 PACK 加载不会首先从文件中加载纹理集（如果它们已经在 pack/ 中），并且对象放置器的对象列表将保持为空，因为它从 property/（而不是从 pack/property）获取列表
; 17) 要保存 regen.txt，请按 CTRL+S
; 18) 如果在 Attr Tab 上启用线框 (f4)，您会看到地形全是白色的
;19）相机渲染水车小/大效果时水刷消失
; 20) 如果你在相关宗门树之外，怪物区域信息将会被隐藏起来
; 21) 仅当添加了顶部图片后才可以显示完整的天空盒（如果已经插入了其他纹理）
; 22) 属性选项卡中的滑块类似于“16 个 photoshop 图层”，您可以在其中拆分属性；有时不太有用，而且相当令人困惑
; 23) 固定模型 - 物体附着点附着静态物体（头发的骨骼不会镜像播放的动画）
; 24) 在环境选项卡中，如果插入较低的梯度，则可能会出现超出范围的崩溃#fixed since v30
; 25) 在屏幕/地图范围外工作的刷子可能会影响随机地形位置
；待办事项：
; A) 查看区域的 8 个以上纹理 -> 完成
; B) 创建快捷方式来修复 #5 注释 -> 完成
；C) 禁用半径 <= GetRadius()+0.0001f 检查以修复 #4 注释 -> REJECTED
；worldeditor_en 调用此断言，如果忽略它，则滞后现象将不复存在（这在源版本中不会发生）
；至少，如果发布版本对你来说不是问题，那么在 .mse 被滥用的少数情况下使用它，并尝试杀死调试版本
; D) 除英语外，翻译成更多语言 -> 拒绝
；英语就足够了！
; E) d 的替代路径：-> REJECTED
；你可以将 d 挂载为 c 的子路径，如下所示：
; 替换 d：“c:\mt2stuff”
；F）需要修复注释#19 #25 -> TODO

[快捷方式]
; ### 快捷方式
; # ESC(ape) 清除光标
; # Canc(el|Delete) 删除选定的建筑物等内容
; # Ctrl+S 保存地图
; # Ins(ert) 或 F6 保存 shadowmap|minimap.dds
; # F3 BoundGrid 显示/隐藏
; # F4 渲染 UI 显示/隐藏
; # F11 线框显示/隐藏
; # R 重新加载纹理
; # Z 和 X 将 Texture Splat 减小/增加 0.1
; # CapsLock 如果显示阴影则显示 GaussianCubic 效果
; # L-Shift+1-6 将 TextureCountThreshold 标志 (&2-7) 显示为地面上的颜色
；# L-Shift+8 将最大可显示纹理设置为 8（修复注释 12）
；# L-Shift+0 将最大可显示纹理设置为 255（修复注释 12）
; # H 刷新 MDATR 高度（移动物体时有用）（修复注释 11）
; # Y 将透视设置为默认值 (修复注释 5)
; # T 设置摄像头捕捉屏幕上的所有物体（带注释 13），然后您就可以按 Insert/F6 了

；# 使用这些快捷方式时没有选择对象（MW1-7）
; # 鼠标滚轮+1 移动光标 x 旋转
; # MouseWheel+2 移动光标 y 旋转
; # 鼠标滚轮+3 移动光标 z 旋转
; # MouseWheel+4 移动光标高度基数 (1x)
; # MouseWheel+5 移动光标高度基数（0.5x）
; # MouseWheel+6 移动光标高度基数（0.05x）
; # 鼠标滚轮+7 移动光标氛围比例 (1x)

; # 鼠标滚轮+Q 移动选定对象的高度基数 (1x)
；# MouseWheel+9 移动选定对象 x 位置 (1x) (+asyncronous)
；# MouseWheel+0 移动选定对象的 y 位置 (1x) (+asyncronous)
；# MW+RSHIFT+9|0 同上但*10x (+异步)
；# MW+RCONTROL+9|0 同上但*100x (+异步)

; # 鼠标左键插入对象
; # MouseRight 移动相机（也可能需要 CTRL）

; # SPACE 在 Object/Effect/Fly CB 中开始移动/选择动画
; # ESC 停止 Effect/Fly CB 中的动画

[配置]
；### 配置选项
VIEW_CHAR_OUTPUT_BY_DEFAULT = 1
VIEW_SHADOW_OUTPUT_BY_DEFAULT = 1
默认查看水输出 = 1

；窗口高度大小 = 1080
；窗口宽度 = 1920
窗口视野大小 = 45

；#100 = 1px（按下 WASD 时最小 px 移动）
WASD_MINIMAL_MOVE = 100

；从按 Insert/F6 之前的位置返回
插入后不可转到 = 1

; 保存图集和/或按 Insert/F6 时禁用 MAI 转储
NOMAI_ATLAS_DUMP = 1

; 禁用 minimap.dds alpha 保存并启用压缩
NOMINIMAP_RAWALPHA = 1

; 在建筑物上移动或调整地形时启用 .mdatr 高度碰撞加载
检测_MDATR_高度 = 1

; 加载地图时禁用雾
NOFOG_ONMAPLOAD = 1

; 加载地图和其他内容时刷新所有复选框配置
REFRESHALL_ONUPDATEUI = 0

; 创建新地图时设置默认的地图名称前缀（“”表示禁用）
NEW_MAP_MAPNAME_PREFIX = "metin2_map_"

; 创建新地图时显示默认纹理集（“”表示禁用）
; 注意：如果存在，它将加载文件路径，否则它将创建一个空的纹理集文件
NEWMAP_TEXTURESETLOADPATH = "纹理集\metin2_a1.txt"

; 创建默认纹理集作为“textureset/{mapname}.txt”
；注意：如果 NEWMAP_TEXTURESETLOADPATH 不为空，则不考虑此选项。[v24 之前]
；注意：如果创建新地图时 TextureSet 路径输入不为空，则不考虑此选项 [自 v24 起]
NEWMAP_TEXTURESETSAVEASMAPNAME = 1

; 从生成的 server_attr 中删除奇怪的 attr 标志
SERVERATTR_REMOVE_WEIRD_FLAGS = 1

; 向物体显示漫射光
视图对象照明 = 1

；用于再生的 mob_proto 路径
MOB_PROTO_PATH = “区域设置/ymir/mob_proto”

; 在启动时选择怪物区域信息复选框
查看怪物区域信息 = 0

；画笔光标/对象选择颜色 RGB 浮点数在 0.0 到 1.0 之间（默认值：绿色 -> 0 1 0）
渲染光标颜色R = 0.0
渲染光标颜色 G = 1.0
渲染光标颜色B = 0.0