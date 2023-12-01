import string
import os
from Bio import SeqIO

fasta_filename = "E:\\HBVdata\\chen_work\\sequence-150kb-invercom-info.fas"
output_folder = "E:\\HBVdata\\chen_work\\"

# 创建"human"和"other"文件夹
human_folder = os.path.join(output_folder, "human")
other_folder = os.path.join(output_folder, "other")
os.makedirs(human_folder, exist_ok=True)
os.makedirs(other_folder, exist_ok=True)

# 读取fasta文件并根据host进行分类
with open(fasta_filename, "r") as input_handle:
    for seq_record in SeqIO.parse(input_handle, "fasta"):
        # 获取host和country信息
        host = seq_record.description.split("host: ")[1].split("\t")[0]
        country = seq_record.description.split("country: ")[1].split("\t")[0]

        # 替换无效字符
        valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
        host = ''.join(c if c in valid_chars else '_' for c in host)
        country = ''.join(c if c in valid_chars else '_' for c in country)

        # 构建完整的输出文件路径
        if host[:4].lower() == "homo":
            output_filename = os.path.join(human_folder, f"{host}_{country}.fasta")
        else:
            output_filename = os.path.join(other_folder, f"{host}_{country}.fasta")

        with open(output_filename, "a") as output_handle:
            SeqIO.write(seq_record, output_handle, "fasta")