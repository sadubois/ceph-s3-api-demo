import java.io.ByteArrayInputStream;
import java.io.File;
import java.util.List;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3Client;
import com.amazonaws.services.s3.model.Bucket;
import com.amazonaws.services.s3.model.CannedAccessControlList;
import com.amazonaws.services.s3.model.GeneratePresignedUrlRequest;
import com.amazonaws.services.s3.model.GetObjectRequest;
import com.amazonaws.services.s3.model.ObjectListing;
import com.amazonaws.services.s3.model.ObjectMetadata;
import com.amazonaws.services.s3.model.S3ObjectSummary;
import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.util.StringUtils;

import com.amazonaws.ClientConfiguration;
import com.amazonaws.Protocol;

public class CephS3Client {
    private static final String SUFFIX = "/";
    public static void main(String[] args) {
        System.out.println("Hello, World!");

    	String accessKey = "F8T4P40OCX8KD96SVDX0";
    	String secretKey = "mSTz7NNOpsn27cc03Rfez+FpHdV2lHn4BinLGG3N";

    	AWSCredentials credentials = new BasicAWSCredentials(accessKey, secretKey);
    	AmazonS3 conn = new AmazonS3Client(credentials);

/*
    	String bucketName = "javatutorial-net-example-bucket";
    	s3client.createBucket(bucketName);
    	s3client.setEndpoint("http://192.168.15.200:7480");
    	conn.setEndpoint("http://192.168.15.200");
*/

    	/*conn.setEndpoint("192.168.15.200:7480");*/
    	conn.setEndpoint("http://192.168.15.200");

    	List<Bucket> buckets = conn.listBuckets();
    	for (Bucket bucket : buckets) {
        	System.out.println(bucket.getName() + "\t" +
                StringUtils.fromDate(bucket.getCreationDate()));
    	}

/*	Bucket bucket = conn.createBucket("my-new-bucket");*/

        System.out.println("ENd!");
    }
}
