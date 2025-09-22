from PIL import Image, ImageDraw, ImageFont
import os

def add_watermark(input_path, output_path, text, font_size=20, font_color='white', position='bottom-right'):
    """
    在图片上添加文字水印
    
    Args:
        input_path (str): 输入图片路径
        output_path (str): 输出图片路径
        text (str): 水印文字
        font_size (int): 字体大小
        font_color (str): 字体颜色
        position (str): 水印位置 (top-left, top-right, bottom-left, bottom-right, center)
    """
    # 打开图片
    image = Image.open(input_path).convert("RGBA")
    width, height = image.size
    
    # 创建透明图层用于绘制水印
    watermark_layer = Image.new("RGBA", image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(watermark_layer)
    
    # 尝试使用系统字体，如果失败则使用默认字体
    try:
        # 在不同系统上尝试不同的字体
        if os.name == 'nt':  # Windows
            font = ImageFont.truetype("arial.ttf", font_size)
        elif os.name == 'posix':  # Unix/Linux/MacOS
            font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", font_size)  # MacOS
        else:
            font = ImageFont.truetype("DejaVuSans.ttf", font_size)  # Linux
    except:
        # 如果找不到指定字体，则使用默认字体
        font = ImageFont.load_default()
    
    # 计算文字尺寸
    try:
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
    except:
        # 兼容旧版本Pillow
        text_width, text_height = draw.textsize(text, font=font)
    
    # 根据位置参数计算水印位置
    margin = 10  # 边距
    if position == 'top-left':
        x, y = margin, margin
    elif position == 'top-right':
        x, y = width - text_width - margin, margin
    elif position == 'bottom-left':
        x, y = margin, height - text_height - margin
    elif position == 'bottom-right':
        x, y = width - text_width - margin, height - text_height - margin
    elif position == 'center':
        x, y = (width - text_width) // 2, (height - text_height) // 2
    else:
        x, y = width - text_width - margin, height - text_height - margin  # 默认为右下角
    
    # 绘制文字水印
    draw.text((x, y), text, font=font, fill=font_color)
    
    # 合并图层
    watermarked_image = Image.alpha_composite(image, watermark_layer)
    
    # 转换为RGB模式以支持JPEG格式
    if output_path.lower().endswith(('.jpg', '.jpeg')):
        watermarked_image = watermarked_image.convert("RGB")
    
    # 保存图片
    watermarked_image.save(output_path)