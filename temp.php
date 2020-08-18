<?php


    /*$file = fopen("temp.txt", "r");

    $content = fgets($file,4096);
    
    echo $content;
    
    fclose($file);

    //echo('test');*/


    try {
        $pdo = new PDO("mysql:host=localhost;dbname=pi3b", "root", "password");
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        
        $sql = 'SELECT temperature FROM releves ORDER BY id_t DESC LIMIT 1; DELETE FROM releves WHERE id_t < (SELECT MAX(id_t) FROM releves) -10'; 
        $results = $pdo->query($sql);
        
        foreach ($results as $row) {
            echo '<tr><td>'.$row[0].'°C'.'</td></tr>';
            echo '<script> result =' . $row[0] . '</script>';
            
            try {
                $pdo = new PDO("mysql:host=localhost;dbname=pi3b", "root", "password");
                $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        
                }
                catch (Exception $e) {
        print("Erreur : " . $e->getMessage());
    }

        }
    }
    catch (Exception $e) {
        print("Erreur : " . $e->getMessage());
    }


?>
