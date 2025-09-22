# 图片水印工具
## 使用方法

### 基本用法

```bash
python src/main.py path/to/your/image.jpg
```

该命令会自动读取图片的EXIF信息中的拍摄时间，并在图片右下角添加时间水印。处理后的图片将保存在原图片目录下的 `_watermark` 文件夹中。

### 自定义参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--font-size` | 设置水印字体大小 | 20 |
| `--font-color` | 设置水印字体颜色 | white |
| `--position` | 设置水印位置，可选值：top-left, top-right, bottom-left, bottom-right, center | bottom-right |

示例：

```bash
# 设置字体大小为30，颜色为红色，位置为左上角
python src/main.py image.jpg --font-size 30 --font-color red --position top-left

# 设置字体大小为25，使用默认位置（右下角）
python src/main.py image.jpg --font-size 25
```

### 输出说明

处理后的图片将保存在原图片目录下的 `_watermark` 子目录中，文件名格式为 `原文件名_watermarked.扩展名`。

例如，处理 `photos/vacation.jpg` 后，输出文件为 `photos/_watermark/vacation_watermarked.jpg`。

## 常见问题

### 1. 运行时出现 "错误: 无法从图片EXIF信息中获取拍摄时间" 怎么办？

这个问题通常出现在以下情况：
- 图片不包含EXIF信息（如截图、网络下载图片等）
- 图片的EXIF信息不完整
- 图片格式不支持EXIF信息

解决方法：
- 确认图片是直接从相机或手机拍摄的原图
- 使用图片查看器检查图片是否包含拍摄时间信息

### 2. 出现 "ModuleNotFoundError: No module named 'PIL'" 错误怎么办？

这是因为缺少 Pillow 库导致的。请运行以下命令安装依赖：

```bash
pip install Pillow
```

或者如果项目包含 requirements.txt 文件：

```bash
pip install -r requirements.txt
```

### 3. 水印文字显示为乱码或方框怎么办？

这是由于系统缺少合适的字体文件导致的。程序会尝试使用系统默认字体，但在某些系统上可能无法正常显示。

解决方法：
- 确保系统安装了常用字体（如 Arial）
- 在 `src/watermark.py` 中修改字体路径，指定一个可用的字体文件

### 4. 生成的图片质量下降了怎么办？

程序会自动保持原图的格式和质量。如果发现质量下降，可能是因为：
- JPEG 图片在保存时采用了默认压缩率
- PNG 图片可能在颜色深度上有所调整

### 5. 支持哪些图片格式？

该工具支持 Pillow 库支持的所有图片格式，包括但不限于：
- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- TIFF (.tiff, .tif)

推荐使用 JPEG 和 PNG 格式的原图以获得最佳效果。

## 许可证

本项目采用 MIT 许可证，详见 [LICENSE](LICENSE) 文件。
</file4>