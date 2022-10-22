<html>
<body>
<table>
% for items in shopping_List:
<tr>
<td>
 {{str(items['id'])}}
 </td>
 <td>
 {{str(items['des'])}}
 </td>
</tr>
% end
</table>
</body>
</html>