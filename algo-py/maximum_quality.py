from unittest import TestCase

def maximumQuality(packets, channels):

    max_quality_return = 0

    packets = sorted(packets) # o(p)
    len_packets = len(packets)


    for idx in range(len_packets - 1, len_packets - channels, -1): # O(p - c)
        max_quality_return += packets[idx]

    len_channels = len_packets - channels + 1

    #smallers packets go on the same channel. so the quality is the median packet directly if odd,
    # if even: consider the two middle packets.
    # odd
    if (len_channels % 2) == 1: max_quality_return += packets[len_channels//2]
    # even
    else: max_quality_return += (packets[len_channels//2] + packets[len_channels//2-1] + 1) //2

    return max_quality_return


TestCase().assertEqual(maximumQuality([5, 2, 2, 1, 5, 3], 3), 12)
TestCase().assertEqual(maximumQuality([5, 2, 2, 1, 5, 3], 2), 7)
