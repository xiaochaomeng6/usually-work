from Bio import SeqIO

gbk_filename = "E:\\HBVdata\\sequence (2).gb"
faa_filename = "E:\\HBVdata\\output_all_human.fasta"

with open(gbk_filename, "r") as input_handle, open(faa_filename, "w") as output_handle:
    #SeqIO.parse参数为（输入文件，“需要迭代的格式”（如genbank，fasta等）
    for seq_record in SeqIO.parse(input_handle, "genbank"):
        #将features这个type中的第一个列表中的信息进行提炼
        isolate = seq_record.features[0].qualifiers.get("isolate", ["*"])[0]
        isolation_source = seq_record.features[0].qualifiers.get("isolation_source", ["*"])[0]
        country = seq_record.features[0].qualifiers.get("country", ["*"])[0]
        host = seq_record.features[0].qualifiers.get("host", ["*"])[0]
        collection_date = seq_record.features[0].qualifiers.get("collection_date", ["*"])[0]
        seq_length = len(seq_record.seq)

        #只收集序列长度大于100的，并且将名字放在前面
        if seq_length > 100:
            record_info = "\t".join([
                f"isolate: {isolate}",
                f"isolation_source: {isolation_source}",
                f"country: {country}",
                f"host: {host}",
                f"collection_date: {collection_date}",
                f"seq_length: {seq_length}"
            ])

            # s作为占位符，将后续record_info和seq_record.seq放入文件中
            output_handle.write(">%s\n%s\n" % (record_info, seq_record.seq))
