
<%--
* @author Adarsh
* @author $LastChangedBy: adarsh $
* @version $Revision: 1595 $, $Date:: 5/4/12 6:12 PM#$
--%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
         pageEncoding="ISO-8859-1" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
    <title>index page</title>
</head>
<body>
<h1>servlet form</h1>
<form action="myGenericServlet">
    Enter the Name<input type="text" name="userName"/>
    <br/><input type="submit" value="send data"/>
</form>
<br/>
<br/>
<h1>jython form</h1>
<form action="jython/JythonServlet.py">
    Enter the Name<input type="text" name="userName"/>
    <br/><input type="submit" value="send data"/>
</form>
</body>
</html>