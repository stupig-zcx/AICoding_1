import os
import sys
import argparse
from PIL import Image, ExifTags
from PIL.ExifTags import TAGS
import datetime

# 添加src目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from watermark import add_watermark
from exif_reader import get_exif_datetime

def main():
    parser = argparse.ArgumentParser(description='给图片添加基于EXIF信息的时间水印')
    parser.add_argument('image_path', help='图片文件路径')
    parser.add_argument('--font-size', type=int, default=20, help='字体大小 (默认: 20)')
    parser.add_argument('--font-color', default='white', help='字体颜色 (默认: white)')
    parser.add_argument('--position', choices=['top-left', 'top-right', 'bottom-left', 'bottom-right', 'center'], 
                        default='bottom-right', help='水印位置 (默认: bottom-right)')
    
    args = parser.parse_args()
    
    # 检查文件是否存在
    if not os.path.exists(args.image_path):
        print(f"错误: 文件 {args.image_path} 不存在")
        return
    
    # 获取EXIF中的拍摄时间
    try:
        datetime_str = get_exif_datetime(args.image_path)
        if not datetime_str:
            print("错误: 无法从图片EXIF信息中获取拍摄时间")
            return
    except Exception as e:
        print(f"错误: 读取EXIF信息时出错: {e}")
        return
    
    # 创建水印目录
    image_dir = os.path.dirname(args.image_path)
    watermark_dir = os.path.join(image_dir, "_watermark")
    
    try:
        os.makedirs(watermark_dir, exist_ok=True)
    except Exception as e:
        print(f"错误: 创建目录 {watermark_dir} 失败: {e}")
        return
    
    # 生成输出文件路径
    image_filename = os.path.basename(args.image_path)
    name, ext = os.path.splitext(image_filename)
    output_path = os.path.join(watermark_dir, f"{name}_watermarked{ext}")
    
    # 添加水印
    try:
        add_watermark(
            input_path=args.image_path,
            output_path=output_path,
            text=datetime_str,
            font_size=args.font_size,
            font_color=args.font_color,
            position=args.position
        )
        print(f"水印添加成功，保存路径: {output_path}")
    except Exception as e:
        print(f"错误: 添加水印时出错: {e}")

if __name__ == "__main__":
    main()