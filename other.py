# # a = [str(x) for x in open('text_for_win_msg.txt', 'r')]
# # print(a)
# import codecs
# # fileObj = codecs.open( "someFilePath", "r", "utf_8_sig" )
# # text = fileObj.read() # или читайте по строке
# # fileObj.close()
#
# with codecs.open('text_for_win_msg.txt', 'r', "utf_8_sig") as file:
#     a = file.readlines()
#     for x in a:
#         x = x.replace('\n', '')
#         x = x.replace('\r', '')
#         print(f' "{x[4::]}",')