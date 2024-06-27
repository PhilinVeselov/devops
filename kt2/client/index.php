<?php
// Запрашиваем содержимое файла с сервера
$content = file_get_contents("http://server:80");
echo $content;
?>
