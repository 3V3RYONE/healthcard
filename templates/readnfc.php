{% extends 'base.html' %}

{% block title %}Details{% endblock %}

{% block style %}
    table, th, td {
        border: 1px solid black;
    }
{% endblock %}

{% block main %}
    <h1>Health Details of Candidate :</h1>
    <table>
        <tr>
            <th> firstName </th>
            <th> lastName </th>
            <th> username </th>
            <th> password </th>
            <th> email </th>
            <th> mobno </th>
            <th> address </th>
            <th> emergencyContact </th>
	    <th> medicalHistory </th>
	    <th> age </th>
	    <th> gender </th>
	    <th> aadharNo </th>
        </tr>
        {% for candidate in details %}
            <tr>
                <td>{{candidate.firstname}}</td>
                <td>{{candidate.lastname}}</td>
                <td>{{candidate.username}}</td>
                <td>{{candidate.password}}</td>
                <td>{{candidate.email}}</td>
                <td>{{candidate.mobno}}</td>
                <td>{{candidate.address}}</td>
                <td>{{candidate.emergencyContact}}</td>
		<td>{{candidate.medicalHistory}}</td>
		<td>{{candidate.age}}</td>
		<td>{{candidate.gender}}</td>
		<td>{{candidate.aadharNo}}</td>
            </tr>
        {% endfor %}
    </table>
{% endblock %}
