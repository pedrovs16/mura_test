// pages/index.tsx
import { useEffect } from "react";
import { useRouter } from "next/router";

const HomePage = () => {
  const router = useRouter();
  useEffect(() => {
    router.push("/admin");
  }, [router]);
  return null;
};

export default HomePage;
