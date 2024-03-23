<?php

use Ujamii\OsmOpeningHours\OsmStringToOpeningHoursConverter;

$hours = OsmStringToOpeningHoursConverter::openingHoursFromOsmString("Mo-Sa 10:00-18:00");
$hours->isOpenAt(new \DateTimeImmutable('2022-01-10 16:00:00')); // true, this is a monday
$hours->isOpenAt(new \DateTimeImmutable('2022-03-06 16:00:00'));

