<?php
            if ($handle = opendir('./')) {
                while (false !== ($file = readdir($handle))) {
                    if ($file != "." && $file != "..") {
                        $thelist .= '<li><a href="'.$file.'">'.$file.'</a></li>';
                    }
                }
            closedir($handle);
            }
        ?>  