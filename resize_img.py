from PIL import Image

# 设置输入输出路径
input_jpg = 'images/Callireader.png'   # 输入的JPG文件路径
output_png = 'images/CalliReader_small.png' # 输出的PNG文件路径

# 读取图片
img = Image.open(input_jpg)

# 调整尺寸到300x300像素（可能改变原图比例）
resized_img = img.resize((500, 350))

# # 保持比例缩放并居中裁剪
# img.thumbnail((300, 300))  # 等比缩放
# width, height = img.size
# left = (width - 300)/2
# top = (height - 300)/2
# right = (width + 300)/2
# bottom = (height + 300)/2
# resized_img = img.crop((left, top, right, bottom))

# 保存为PNG格式
resized_img.save(output_png)

print(f"图片已压缩至300x300像素并保存为 {output_png}")

# from PIL import Image

# def convert_png_to_ico(input_path, output_path):
#     """
#     将PNG图片转换为48x48的ICO文件。

#     :param input_path: 输入PNG图片的路径
#     :param output_path: 输出ICO文件的路径
#     """
#     try:
#         # 打开PNG图片
#         img = Image.open(input_path)
        
#         # 调整图片大小为48x48，使用Image.LANCZOS替代Image.ANTIALIAS
#         img = img.resize((48, 48), Image.LANCZOS)
        
#         # 保存为ICO格式
#         img.save(output_path, format="ICO", sizes=[(48, 48)])
        
#         print(f"成功将图片转换为ICO文件：{output_path}")
#     except Exception as e:
#         print(f"发生错误：{e}")

# # 示例用法
# if __name__ == "__main__":
#     input_png = "images/logo.png"  # 替换为你的PNG文件路径
#     output_ico = "images/logo.ico"  # 替换为你希望保存的ICO文件路径
#     convert_png_to_ico(input_png, output_ico)