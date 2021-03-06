Some of the tools i'm using in day-to-day development - Residing in ~/bin, along with some installations, as follows:

# General Tools
* `colcount` - Converts standard input lines to their respective column counts
* `q` - See https://github.com/harelba/q
* `secs2date` - Converts timestamps to human date-time strings
* `sigma` - Sums up all the numbers from stdin
* `xvsy` - Draws an XY graph of x values vs y values - Getting pairs of x,y lines from standard input
* `categoryvsy` - Draws a bar graph for category names vs y values - Getting pairs of category-name,y lines from standard input
* `display` - Uses disper in order to control multiple monitor setups for the same machine (docked, undocked,home etc.)
* `disable-company-settings/enable-company-settings` - Allow quick switching between a company provided maven settings.xml and a default one
* `svn-diff-meld` - Wrapper so svn would work with meld
* `mvn-test-multiple` - Run a test using maven multiple times, each time saving the log file and the test results to separate files
* `groupby` - Count lines per distinct data value in column number colnumber.
* `hive-table-fields-to-pig-load-command` - Converts the output of a hive DESCRIBE command into a Pig LOAD command

# Zookeeper related utilities:
* `zkfind` - get a zookeeper path and lists all nodes recursively, similar to linux find
* `zkget` - gets the data of a specific node in zookeeper
* `zkrmr` - Performs a recusrive delete of zookeeper nodes (this capability is included in zkCli if you're using zookeeper >3.4)
* `zkgrep` - Finds a substring in the data of zookeeper nodes

# Installations (not included in this source code obviously):
* apache-maven-2.2/
* apache-maven-3/
* apache-maven/
* apache-tomcat-2nd-instance/
* apache-tomcat/
* eclipse-plugins/
* eclipse/
* hadoop-0.20.2-cdh3u3/
* hive-0.8.1/
* sqoop-1.3.0-cdh3u3/
* storm-0.7.2/
* kafka-0.7.0-incubating-src/
* pig-0.10.0/
* apache-cassandra-1.1.0/
* apache-activemq-5.4.3/
* zookeeper-3.3.5/


