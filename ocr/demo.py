import easyocr
import os


# 封装OCR识别的功能
def perform_ocr(image_path, lang_list=["ch_sim"]):
    """
    使用EasyOCR读取图片中的文本。

    :param image_path: 图片的路径
    :param lang_list: 语言列表，默认为简体中文
    :return: 识别结果，成功则返回识别到的文本列表，失败则返回错误信息
    """
    try:
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"文件 {image_path} 不存在。")

        # 初始化OCR读取器
        reader = easyocr.Reader(lang_list)

        # 执行OCR识别
        result = reader.readtext(image_path)

        return result

    except FileNotFoundError as e:
        return f"文件错误: {e}"

    except Exception as e:
        return f"发生错误: {e}"


# 主函数
if __name__ == "__main__":
    image_path = "D:\\temp\\3.png"  # 可以根据需要修改为其他路径
    lang_list = ["ch_sim"]  # 使用简体中文

    # 执行OCR并打印结果
    result = perform_ocr(image_path, lang_list)
    print(result)
