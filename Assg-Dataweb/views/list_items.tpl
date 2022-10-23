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
 <td>
 <a href="/delete/{{str(items['id'])}}">del</a>
 </td>
 <td>
 <a href="/edit/{{str(items['id'])}}">edit</a>
 </td>
</tr>
% end
</table>
<hr>
<a href="/addFood">New Items..</a>
</body>
</html>