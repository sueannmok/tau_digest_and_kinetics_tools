#! /usr/bin/perl -w
# Translate to grace format


open (file1, "log.txt") || die "Could not open input file";
open (file2, ">log-formatted.txt") || die "Could not open input file";

while (<file1>)
        {
	push(@list1, $_);
        }

$i = 0;

while ($list1[$i])
        {
	$line1 = $list1[$i];
	chop $line1;

	# print title
	if (($line1 !~ /^\t/) & ($line1 !~ /Chi/) & ($line1 !~ /Correlation/) & ($line1 !~ /RMS/))
		{
		if ($line1 =~ /\d/) 
			{
			print "\n$line1,";
			print file2 "\n$line1,";
			}
		}

	# print stats
	if ($line1 =~ /^\t/)
		{
		$line1 =~ s/\ta. = //g;
		if ($line1 =~ /\d/) 
			{
			print "$line1,";
			print file2 "$line1,";
			}

		}

	# print fit stats
	if (($line1 =~ /Chi/) || ($line1 =~ /Correlation/) || ($line1 =~ /RMS/))
		{
		$line1 =~ s/Chi-square: //g;
		$line1 =~ s/Correlation coefficient: //g;
		$line1 =~ s/RMS relative error: //g;
		print "$line1,";
		print file2 "$line1,";
		}
	$i++;
	}

print "\n";
print file2 "\n";

close (file1);
close (file2);
