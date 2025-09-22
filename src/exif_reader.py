from PIL import Image, ExifTags
from PIL.ExifTags import TAGS
import datetime

def get_exif_datetime(image_path):
    """
    从图片EXIF信息中获取拍摄时间
    
    Args:
        image_path (str): 图片文件路径
        
    Returns:
        str: 格式化的拍摄时间 YYYY-MM-DD，如果无法获取则返回None
    """
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        
        if exif_data is None:
            return None
            
        # 查找拍摄时间相关的EXIF标签
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            # 常见的拍摄时间标签
            if tag in ["DateTime", "DateTimeOriginal", "DateTimeDigitized"]:
                # 尝试解析时间字符串
                try:
                    # EXIF时间格式通常是 "YYYY:MM:DD HH:MM:SS"
                    dt = datetime.datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
                    return dt.strftime("%Y-%m-%d")
                except ValueError:
                    continue
        
        return None
    except Exception as e:
        raise Exception(f"读取EXIF信息失败: {str(e)}")