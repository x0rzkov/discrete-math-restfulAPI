import base64
from io import BytesIO

import matplotlib_venn as vplt
from PIL import Image
from matplotlib import pyplot as plt

import io




def ven2():
    """Venn Diagram example for 2 sets"""

    num_gen1 = random_gen(3, 12)
    num_gen2 = random_gen(6, 25)
    set1 = set()
    set2 = set()
    # try to add elem to set until set length is less than 3
    for x in itertools.takewhile(lambda x: len(set1) < 7, num_gen1):
        set1.add(x)
    for x in itertools.takewhile(lambda x: len(set2) < 10, num_gen2):
        set2.add(x)
    print('A : ' + str(set1) + ' , B : ' + str(set2))

    # length of sets for venn diagram
    a = len(set1)
    b = len(set2)
    c = len(set1.intersection(set2))
    print('Intersection : ' + str(set1.intersection(set2)))

    # Venn Diagram
    v = vplt.venn2(subsets={'10': a, '01': b, '11': c}, set_labels=('A', 'B'))
    l1 = ','.join(map(str, set1.difference(set2)))
    v.get_label_by_id('10').set_text(l1)
    l2 = ','.join(map(str, set2.difference(set1)))
    v.get_label_by_id('01').set_text(l2)
    l3 = ','.join(map(str, set2.intersection(set1)))
    v.get_label_by_id('11').set_text(l3)
    # img_link = 'https://regform2020.s3.us-east-2.amazonaws.com/' + filename

    # s = io.BytesIO()

    plt.savefig('figure.png')
    plt.close()
   # s = base64.b64encode(s.getvalue()).decode("utf-8").replace("\n", "")
    encoded = str(base64.b64encode(open("figure.png", "rb").read())).replace("b'"," ").replace("'","")
    img = 'data:image/png;base64,%s' % encoded

    return img

