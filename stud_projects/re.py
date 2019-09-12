import re

re.findall(r'A.?', 'AV Analytics Vidhya AV  A')

"".join(re.findall(r'[\w ]+', 'AV , >Ana?lytics!/ Vidhy:a AV  A'))

re.findall(r'[\d ]+', 'AV Anal45ytics56  Vidhya945876 AV  A')

re.findall(r'^\w+', 'AV Anal45ytics56  Vidhya945876 AV  A')

re.findall(r'\b\w{2}', 'AV Anal45ytics56  Vidhya945876 AV  A')

re.findall(r'\w{2}\b', 'AV Anal45ytics56  Vidhya945876 AV  A')

re.findall(r'@\w+(\.\w+)', 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')

re.findall(r'\b(\w+)\.\w+@', 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')

re.findall(r'\d\d[-/]\d\d[-/]\d\d\d\d', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011  11411/2011  11/11/2011, ABC 67-8945 12-01-2009')

re.findall(r'\d\d\W\d\d\W(\d{4})', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011  11411/2011  11/11/2011, ABC 67-8945 12-01-2009')

re.findall(r'\b[aoiueyAOIUEY]\w+', 'AV is largest Analytics community of India')

re.findall(r'(\d+)([A-Z]\D+)([A-Z]\D+)', '1NoahEmma2LiamOlivia3MasonSophia4JacobIsabella5WilliamAva6EthanMia7MichaelEmily')