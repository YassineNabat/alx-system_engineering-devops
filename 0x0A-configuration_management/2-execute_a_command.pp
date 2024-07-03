# execute pkill command to kill bashscript file killmenow

exec { 'pkill killmenow' :
    path    => '/bin/',
    command => 'pkill killmenow',
    }
