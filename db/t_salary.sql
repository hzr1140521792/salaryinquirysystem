/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50709
Source Host           : localhost:3306
Source Database       : salary

Target Server Type    : MYSQL
Target Server Version : 50709
File Encoding         : 65001

Date: 2017-12-08 18:28:30
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `t_salary`
-- ----------------------------
DROP TABLE IF EXISTS `t_salary`;
CREATE TABLE `t_salary` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `school_no` int(11) DEFAULT NULL,
  `attendance_percent` float(11,2) DEFAULT NULL,
  `attendance_salary` double DEFAULT NULL,
  `station` varchar(255) DEFAULT NULL,
  `station_salary` double DEFAULT NULL,
  `appearence` varchar(255) DEFAULT NULL,
  `appearence_salary` double DEFAULT NULL,
  `business_salary` double DEFAULT NULL,
  `overtime_salary` double DEFAULT NULL,
  `sum_salary` double DEFAULT NULL,
  `real_salary` double DEFAULT NULL,
  `salary` double DEFAULT NULL,
  `month` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=92 DEFAULT CHARSET=utf8;

