<?php
$a = false;
$b = true;
$c = !false;

if (($a || $b) && $c) {
    echo "puede espiar";
} else {
    echo "No puede espiar";
}
?>
