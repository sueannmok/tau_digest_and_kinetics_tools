#! /usr/bin/perl
#
# Olivier Julien, 2014

open (file1, "$ARGV[0]") || die "Could not open input file";

while (<file1>)
	{
	# title
	if ($_ =~ m/time/)
		{
		$_ =~ s/ /_/g;
		push (@full_title, $_);
		@title = split(/\t/, $_);
		}
	else
		{
		push (@data, $_);
		@input_line = split(/\t/, $_);
		push (@time, $input_line[0]);
		}
	}

$j=1;
$count = 0;

while ($title[$j])
	{
	$count = $count+1;
	# open new file
	# set file name

	$file_name = "$title[$j]_$count";
	open (output_file1, ">./data/$file_name.dat") || die "Could not open output file";

	# print title
	print "\@title \"$title[$j]_$count\"\n";
	print output_file1 "\@title \"$title[$j]_$count\"\n";

	$i=0;
	while ($data[$i]) # Go through skyline file
		{
		@data_line = split(/\t/, $data[$i]);
	
		# calculate average
			
		# print
#		print "$time[$i] \t $data_line[$j] \n";
		if ($data_line[$j])
			{
			print output_file1 "$time[$i] \t $data_line[$j] \n";
			}
		$i++;
		}


	if ($count == 3) {$count = 0;}
	close "output_file1";
	$j++;
	}

close "file1";
