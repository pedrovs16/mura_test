// pages/admin.tsx
import dynamic from "next/dynamic";

const DynamicPage = dynamic(() => import("./CombinedPage"), {
  ssr: false,
});

export default DynamicPage;
