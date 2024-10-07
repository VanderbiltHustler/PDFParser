import React, { useState } from 'react';
import { Box, Button, Text, VStack, useColorModeValue } from '@chakra-ui/react';
import { useDropzone } from 'react-dropzone';

const PDFUploader = () => {
  const [file, setFile] = useState(null);
  const [uploadStatus, setUploadStatus] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  // Handling file selection via Dropzone
  const onDrop = (acceptedFiles) => {
    const selectedFile = acceptedFiles[0];
    setFile(selectedFile);
    setUploadStatus(''); // Reset status when a new file is selected
  };

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: 'application/pdf',
    maxFiles: 1,
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) {
      alert('Please select a file first');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    setIsLoading(true); // Start loading spinner

    try {
      const response = await fetch('/upload', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        const blob = await response.blob();
        const url = window.URL.createObjectURL(new Blob([blob]));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', `${file.name.split('.')[0]}.xlsx`);
        document.body.appendChild(link);
        link.click();
        link.parentNode.removeChild(link);
        setUploadStatus('File converted successfully!');
      } else {
        setUploadStatus('Error converting the file. Please try again.');
      }
    } catch (error) {
      console.error('Error uploading file:', error);
      setUploadStatus('Error uploading file.');
    }

    setIsLoading(false); // Stop loading spinner
  };

  return (
    <Box
      maxW="md"
      mx="auto"
      pl={6}
      pr={6}
      pt={6}
      border="1px solid"
      borderColor="gray.300"
      borderRadius="lg"
      textAlign="center"
    >
      <Text fontSize="xl" mb={4}>
        Upload your tabular PDF and a CSV will be downloaded promptly
      </Text>

      {/* Dropzone area */}
      <Box
        {...getRootProps()}
        borderWidth={2}
        borderRadius="md"
        borderColor={isDragActive ? 'blue.500' : 'gray.300'}
        pt={6}
        mb={4}
        bg={useColorModeValue('gray.50', 'gray.700')}
        cursor="pointer"
        textAlign="center"
      >
        <input {...getInputProps()} />
        {isDragActive ? (
          <Text>Drop the PDF file here...</Text>
        ) : (
          <Text>
            Drag and drop a PDF file here, or click to select one
          </Text>
        )}
      </Box>

      {file && (
        <Text fontSize="md" color="green.500">
          Selected File: {file.name}
        </Text>
      )}

      <Button
        onClick={handleSubmit}
        isLoading={isLoading}
        loadingText="Uploading"
        colorScheme="blue"
        isDisabled={!file || isLoading}
        mt={0}
      >
        Upload
      </Button>

      <Text mt={2} color={uploadStatus.includes('success') ? 'green.500' : 'red.500'}>
        {uploadStatus}
      </Text>
    </Box>
  );
};

export default PDFUploader;
