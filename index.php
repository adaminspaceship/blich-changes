<?php
$day = date('w');
$lessons = array();
//Receive the RAW post data via the php://input IO stream.
$content = file_get_contents("php://input");
$json = json_decode($content, true);
//echo $json["result"]["parameters"]["day"];
$school = file_get_contents("lessons.json");
$jsons = json_decode($school, true);
foreach ($jsons[$day] as $field => $value)
 {
    $lessons[] = $value;
};

$new = array(
            "source" => $json["result"]["source"],
            "speech" => implode(", ",$lessons),
            "displayText" => ".........TEXT HERE...........",
            "contextOut" => array()
        );
header("Content-type: application/json");
echo json_encode($new, JSON_UNESCAPED_SLASHES);
?>
