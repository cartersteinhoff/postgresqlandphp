<?php
$config = parse_ini_file('config.ini');

$host = $config['host'];
$database = $config['database'];
$user = $config['user'];
$password = $config['password'];

$connection = pg_connect("host=$host dbname=$database user=$user password=$password");


if (!$connection) {
    echo "Error connecting to the database.";
    exit;
}

$query = "SELECT * FROM languages";
$result = pg_query($connection, $query);

if (!$result) {
    echo "Error executing the query.";
    exit;
}

echo "<table>";
echo "<tr><th>ID</th><th>Language</th></tr>";

while ($row = pg_fetch_assoc($result)) {
    echo "<tr>";
    echo "<td>" . $row['id'] . "</td>";
    echo "<td>" . $row['name'] . "</td>";
    echo "</tr>";
}

echo "</table>";

pg_free_result($result);
pg_close($connection);
?>