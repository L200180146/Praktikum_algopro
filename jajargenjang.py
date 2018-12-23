def hitung_luas():
    'fungsi menghitung luas jajargenjang'
    a=10
    t=15
    luas= a*t
    return luas

print '<!DOCTYPE html>'
print
print '''<html>
<head>
    <title> Bangun Geometri </title>
</head> '''
print '<body> <table> <tr>'
print '<td> <img src="a.jpg" width="100" height="150"> </img> </td>'
print '<td> <h1> BANGUN GEOMETRI </h1>'
print 'Nama Bangun: Jajargenjang </br>'
print 'Dimensi: 2D </br>'
print 'Rumus luas: a x t </br>'
print 'alas: 12 </br>'
print 'tinggi: 17 </br>'
print 'Luas: ', hitung_luas()
print '''</td>
</tr>
</table>'''
print '</body> </html>'
