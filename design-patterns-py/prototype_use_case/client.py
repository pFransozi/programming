from document import Document

ORIGINAL_DOC = Document('Original', [[1,2,3,4],[5,6,7,8,9]])
print(ORIGINAL_DOC)
print()

DOC_COPY_1 = ORIGINAL_DOC.clone(1)
DOC_COPY_1.name = 'Copy 1'
DOC_COPY_1.list[1][2] = 200
print(DOC_COPY_1)
print(ORIGINAL_DOC)
print()

DOC_COPY_2 = ORIGINAL_DOC.clone(2)
DOC_COPY_2.name = 'Copy 2'
DOC_COPY_2.list[1] = [101, 201, 301, 401, 501]
print(DOC_COPY_2)
print(ORIGINAL_DOC)
print()

DOC_COPY_3 = ORIGINAL_DOC.clone(2)
DOC_COPY_3.name = 'Copy 3'
DOC_COPY_3.list[0][0] = "123456789"
print(DOC_COPY_3)
print(ORIGINAL_DOC)
print()

DOC_COPY_4 = ORIGINAL_DOC.clone(3)
DOC_COPY_4.name = 'Copy 4'
DOC_COPY_4.list[1][0] = '09876654321'
print(DOC_COPY_4)
print(ORIGINAL_DOC)
print()
